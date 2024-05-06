# items.py

class Item:
    instances = []
    def __init__(self, nome, preco_mercado, preco_craft, cidade, encantamento):
        self.nome = nome
        self.preco_mercado = preco_mercado
        self.preco_craft = preco_craft
        self.cidade = cidade
        self.encantamento = encantamento
        Item.instances.append(self)


class CraftingSlot:
    instances = []
    # [Lista com todas as recipies, temporaria até nao termos PostGres]

    def __init__(self, craft_id, item_destino_nome, qtd, item_source_nome):
        self.craft_id = craft_id
        self.item_destino_nome = item_destino_nome
        self.qtd = qtd
        self.item_source_nome = item_source_nome
        CraftingSlot.instances.append(self)


