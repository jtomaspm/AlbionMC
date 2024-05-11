from src.core.entities.item import Item


class ItemService:
    def set_attributes_from_unique_name(self, item: Item):
        if item.unique_name[0] == 'T' and item.unique_name[1].isdigit():
            item.tier = int(item.unique_name[1])
        if item.unique_name[-2] == "@" and item.unique_name[-1].isdigit():
            item.enchant = int(item.unique_name[-1])