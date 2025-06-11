import requests
import xml.etree.ElementTree as ET
import logging
import psycopg2
from psycopg2.extras import execute_values

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_crafting_data():
    url = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/refs/heads/master/items.xml"
    resp = requests.get(url)
    resp.raise_for_status()
    root = ET.fromstring(resp.text)
    
    recipes = []
    for item in root.findall('.//*[@uniquename]'):
        uniquename = item.get('uniquename')
        if not uniquename:
            continue
        uniquename = uniquename.strip()
        enchant = int(item.get('enchantmentlevel', 0))
        
        craft = item.findall('craftingrequirements')
        if not craft:
            continue
        
        for craft in craft:
            silver_cost = int(craft.get('silver', 0))
            craft_time = float(craft.get('time', 0))
            focus_cost = float(craft.get('craftingfocus', 0))
            
            ingredients = []
            for ing in craft.findall('craftresource'):
                ing_name = ing.get('uniquename')
                count = int(ing.get('count', 1))
                ing_enchant = int(ing.get('enchantmentlevel', 0))
                ing_max_return = int(ing.get('maxreturnamount', -1))
                ingredients.append((ing_name, count, ing_enchant, ing_max_return))
            
            recipes.append((uniquename, enchant, silver_cost, craft_time, focus_cost, ingredients))
    return recipes

def migrate(conn):
    data_source_id = 2
    updated_by = 'DataSeed'
    created_by = 'DataSeed'
    
    recipes = get_crafting_data()
    with conn.cursor() as cur:
        for uniquename, enchant, silver_cost, craft_time, focus_cost, ingredients in recipes:
            cur.execute("""
                SELECT id FROM items
                WHERE unique_name = %s AND enchant = %s
                """, (uniquename, enchant))
            row = cur.fetchone()
            if not row:
                logger.warning(f"Item not found for recipe: {uniquename}@{enchant}")
                continue
            item_id = row[0]
            
            cur.execute("""
                INSERT INTO item_recipes (item_id, silver_cost, craft_time, focus_cost,
                                         updated_by, created_by, data_source_id)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (item_id) DO UPDATE
                  SET silver_cost = EXCLUDED.silver_cost,
                      craft_time = EXCLUDED.craft_time,
                      focus_cost = EXCLUDED.focus_cost,
                      updated_by = EXCLUDED.updated_by,
                      updated_at = CURRENT_TIMESTAMP,
                      data_source_id = EXCLUDED.data_source_id
            """, (item_id, silver_cost, craft_time, focus_cost,
                  updated_by, created_by, data_source_id))
            
            cur.execute("SELECT id FROM item_recipes WHERE item_id = %s", (item_id,))
            recipe_id = cur.fetchone()[0]
            
            cur.execute("DELETE FROM recipe_slots WHERE recipe_id = %s", (recipe_id,))
            slot_tuples = []
            for ing_name, count, ing_enchant, ing_max_return in ingredients:
                cur.execute("SELECT id FROM items WHERE unique_name = %s AND enchant = %s", (ing_name,ing_enchant))
                ing_row = cur.fetchone()
                if not ing_row:
                    logger.warning(f"Ingredient item not found: {ing_name}")
                    continue
                ing_item_id = ing_row[0]
                slot_tuples.append((recipe_id, ing_item_id, count, ing_max_return))
            if slot_tuples:
                execute_values(cur, """
                    INSERT INTO recipe_slots (recipe_id, item_id, item_count, max_return)
                    VALUES %s
                """, slot_tuples)
    
    conn.commit()

if __name__ == "__main__":
    with psycopg2.connect(dbname='AlbionMC', user='postgres', password='postgres123', host='localhost', port='5432') as conn:
        try:
            migrate(conn)
            logger.info("Crafting recipes import complete.")
        except Exception as e:
            logger.exception("Error during recipes migration")