
def get_data() -> list[dict]:
    import requests
    url = "https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.txt"

    response = requests.get(url)
    response.raise_for_status()

    lines = response.text.strip().splitlines()

    parsed_items = []
    for line in lines:
        parts = line.split(":")
        if len(parts) >= 3:
            item_id = parts[0].strip()
            unique_name = parts[1].strip()
            english_name = ":".join(parts[2:]).strip()
        elif len(parts) == 2:
            item_id = parts[0].strip()
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
            enchant = int(parts[1].strip())

        parsed_items.append({
            "id": item_id,
            "unique_name": unique_name,
            "english_name": english_name,
            "tier": tier,
            "enchant": enchant
        })

    return parsed_items

from psycopg2.extensions import connection
def migrate(conn: connection):
    with conn.cursor() as cur:
        for item in get_data():
            try:
                cur.execute("""
                    INSERT INTO items (unique_name, english_name, tier, enchant, updated_by, created_by, data_source_id)
                    VALUES (%s, %s, %s, %s, 'DataSeed', 'DataSeed', 2);
                """, (item['unique_name'], item['english_name'], item['tier'], item['enchant']))
                conn.commit()
            except Exception as e:
                print(f"Failed to insert item {item['unique_name']}: {e}")