
class CraftingSlot:
    instances = []
    # [Lista com todas as recipies, temporaria até nao termos PostGres]

    def __init__(self, craft_id, item_destino_nome, qtd, item_source_nome):
        self.craft_id = craft_id
        self.item_destino_nome = item_destino_nome
        self.qtd = qtd
        self.item_source_nome = item_source_nome
        CraftingSlot.instances.append(self)

