import os
import sys

from src.service.file_service import FileService
from src.core.item import Item, ItemBuilder
from src.dependencies import configure_injector
from injector import Injector

# Add the project's root directory to the Python path
current_dir = os.path.dirname(os.path.realpath(__file__))
project_root = os.path.abspath(os.path.join(current_dir, '../../../'))
sys.path.append(project_root)



class ItemLoader:
    fs: FileService
    def __init__(self, injector: Injector) -> None:
        self.fs = injector.get(FileService)

    def load_items(self, source: str):
        file_path = os.path.join(current_dir,"temp/items.txt")

        self.fs.download_raw_file(
            url       = source,
            save_path = file_path
            )

        i = 0
        ib = ItemBuilder()
        for line in self.fs.read_file(file_path=file_path):
            la = [i.strip() for i in line.split(":")]
            ib.set_item(Item()).set_unique_name(la[1])
            if len(la)>2:
                ib.set_name(la[2])
            item = ib.build()
            print(item.unique_name)
            if i == 10:
                break

        self.fs.delete_file(file_path=file_path)

if __name__ == "__main__":
    ItemLoader(injector=configure_injector()).load_items("https://raw.githubusercontent.com/ao-data/ao-bin-dumps/master/formatted/items.txt")