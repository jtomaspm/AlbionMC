import os
import sys

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.append(project_root)


import src.backend.service.file_service as fs
from src.backend.core.item import Item, ItemBuilder


def load_items(source: str):
    file_path = os.path.join(current_dir,"temp/items.txt")

#    fs.download_raw_file(
#        url       = source,
#        save_path = file_path
#        )

    i = 0
    ib = ItemBuilder()
    for line in fs.read_file(file_path=file_path):
        la = [i.strip() for i in line.split(":")]
        ib.set_item(Item()).set_unique_name(la[1])
        if len(la)>2:
            ib.set_name(la[2])
        item = ib.build()
        if i == 10:
            break

    #fs.delete_file(file_path=file_path)

if __name__ == "__main__":
    load_items("https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.txt")