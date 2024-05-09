
from typing import List


class Item:
    id          :int | None
    unique_name :str
    name        :str
    tags        :List[str]
    tier        :int
    enchant     :int
    description :str
    def __init__(self) -> None:
        self.id = None          
        self.unique_name = ""
        self.name = ""       
        self.tier = 0       
        self.enchant = 0    
        self.description = ""
        self.tags = []

class ItemBuilder:
    item: Item
    def __init__(self, item: Item = None) -> None:
        if item:
            self.item = item
        else:
            self.item = Item()

    def set_item(self, item: Item):
        self.item = item
        return self
    
    def set_id(self,id: int):
        self.item.id = id
        return self
    
    def set_unique_name(self,unique_name:str):
        self.item.unique_name = unique_name
        if unique_name[0] == 'T' and unique_name[1].isdigit():
            self.set_tier(int(unique_name[1]))
        if unique_name[-2] == "@" and unique_name[-1].isdigit():
            self.set_enchant(int(unique_name[-1]))
        return self

    def set_name(self,name:str):
        self.item.name = name
        return self

    def add_tag(self,tag:str):
        self.item.tags.append(tag)
        return self

    def set_tier(self,tier:int):
        self.item.tier = tier
        return self

    def set_enchant(self,enchant:int):
        self.item.enchant = enchant
        return self

    def set_description(self,desc:str):
        self.item.description = desc
        return self

    def build(self):
        return self.item

class Item_OLD:
    instances = []
    def __init__(self, nome, preco_mercado, preco_craft, cidade, encantamento):
        self.nome = nome
        self.preco_mercado = preco_mercado
        self.preco_craft = preco_craft
        self.cidade = cidade
        self.encantamento = encantamento
        Item_OLD.instances.append(self)