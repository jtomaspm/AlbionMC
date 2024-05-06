class Item:
    instances = []
    def __init__(self, nome, preco_mercado, preco_craft, cidade, encantamento):
        self.nome = nome
        self.preco_mercado = preco_mercado
        self.preco_craft = preco_craft
        self.cidade = cidade
        self.encantamento = encantamento
        Item.instances.append(self)