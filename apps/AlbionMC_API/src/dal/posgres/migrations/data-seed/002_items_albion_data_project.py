def get_data() -> list[tuple]:
    import requests
    import xml.etree.ElementTree as ET
    url = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.txt"

    response = requests.get(url)
    response.raise_for_status()

    lines = response.text.strip().splitlines()

    parsed_items = {}
    for line in lines:
        parts = line.split(":")
        if len(parts) >= 3:
            unique_name = parts[1].strip()
            english_name = ":".join(parts[2:]).strip()
        elif len(parts) == 2:
            unique_name = parts[1].strip()
            english_name = ""
        else:
            print(f"Skipping malformed line: {line}")
            continue

        tier = unique_name.split("_")[0]
        if tier.startswith("UNIQUE"):
            tier = 0
        elif tier.startswith("SKIN"):
            tier = -1
        elif tier.startswith("TREASURE"):
            tier = -2
        elif tier.startswith("PLAYERISLAND"):
            tier = -3
        elif tier.startswith("QUESTITEM"):
            tier = -4
        elif tier.startswith("T"):
            tier = int(tier[1:])
        else:
            print(f"Unknown tier format in line: {line}")
            tier = -100

        parts = unique_name.split("@")
        enchant = 0
        if len(parts) > 1:
            unique_name = parts[0].strip()
            enchant = int(parts[1].strip())

        if parsed_items.get(unique_name):
            parsed_items[unique_name][enchant] = ({
                'unique_name': unique_name,
                'english_name': english_name,
                'tier': tier,
                'enchant': enchant,
                'tags': [],
                'updated_by': 'DataSeed',
                'created_by': 'DataSeed',
                'data_source_id': 2,
            })
        else:
            parsed_items[unique_name] = {
                enchant: {
                    'unique_name': unique_name,
                    'english_name': english_name,
                    'tier': tier,
                    'enchant': enchant,
                    'tags': [],
                    'updated_by': 'DataSeed',
                    'created_by': 'DataSeed',
                    'data_source_id': 2,
                }
            }

    unique_name = None
    url = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/refs/heads/master/items.xml"

    response = requests.get(url)
    response.raise_for_status()

    content = response.text.strip()
    root = ET.fromstring(content)

    data = []
    for item in root.findall('.//*[@uniquename]'):
        unique_name = item.get('uniquename')
        if not unique_name:
            continue
        unique_name = unique_name.strip()
        tags = []
        tag = item.tag
        shopcategory = item.get('shopcategory')
        shopsubcategory1 = item.get('shopsubcategory1')
        kind = item.get('kind')
        enchantmentlevel = item.get('enchantmentlevel')
        tier = item.get('tier')
        if tag:
            tags.append(tag.strip())
        if shopcategory:
            tags.append(shopcategory.strip())
        if shopsubcategory1:
            tags.append(shopsubcategory1.strip())
        if kind:
            tags.append(kind.strip())
        tags = list(set(tags))

        item_block = parsed_items.get(unique_name)
        if not item_block:
            parsed_items[unique_name] = {
                int(enchantmentlevel) if enchantmentlevel else 0 : {
                    'unique_name': unique_name,
                    'english_name': item.get('englishname', ''),
                    'tier': int(tier) if tier else -100,
                    'enchant': int(enchantmentlevel) if enchantmentlevel else 0,
                    'tags': tags,
                    'updated_by': 'DataSeed',
                    'created_by': 'DataSeed',
                    'data_source_id': 2,
                }
            }
        else:
            item_data = item_block.get(int(enchantmentlevel) if enchantmentlevel else 0)
            if item_data:
                item_data['tags'] = tags
                item_data['enchant'] = int(enchantmentlevel) if enchantmentlevel else item_data['enchant']
                item_data['tier'] = int(tier) if tier else item_data['tier']
                parsed_items[unique_name][item_data['enchant']] = item_data
            else:
                parsed_items[unique_name][int(enchantmentlevel) if enchantmentlevel else 0] = {
                    'unique_name': unique_name,
                    'english_name': item.get('englishname', ''),
                    'tier': int(tier) if tier else -100,
                    'enchant': int(enchantmentlevel) if enchantmentlevel else 0,
                    'tags': tags,
                    'updated_by': 'DataSeed',
                    'created_by': 'DataSeed',
                    'data_source_id': 2,
                }

    for unique_name in parsed_items.keys(): 
        tags = []
        for enchant in parsed_items[unique_name].keys():
            if len(tags) == 0:
                tags = parsed_items[unique_name][enchant]['tags']

        for enchant in parsed_items[unique_name].keys():
            item = parsed_items[unique_name][enchant]
            data.append((
                item['unique_name'], 
                item['english_name'], 
                item['unique_name'] if item['enchant'] < 1 else item['unique_name'] + '@' + str(item['enchant']),
                tags, 
                item['tier'], 
                item['enchant'], 
                item['updated_by'], 
                item['created_by'], 
                item['data_source_id']
            ))

    return data

from psycopg2.extensions import connection
def migrate(conn: connection):
    from psycopg2.extras import execute_values
    try:
        with conn.cursor() as cur:
            data = get_data()
            execute_values(cur, """
                INSERT INTO items (unique_name, english_name, item_description, tags, tier, enchant, updated_by, created_by, data_source_id)
                VALUES %s
            """, data, page_size=1000)
            conn.commit()
    except Exception as e:
        print(f"Failed to insert items: {e}")

import psycopg2
if __name__ == "__main__":
    get_data()
    with psycopg2.connect(dbname='AlbionMC', user='postgres', password='postgres123', host='localhost', port='5432') as conn:
        migrate(conn)