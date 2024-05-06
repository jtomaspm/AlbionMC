from backend.core.Item import Item, CraftingSlot

Steel_Bar = Item("Steel Bar", 270, 400, "Lymhurst", 0)
Adepts_Soldier_Boots = Item("Adept's Soldier Boots", 3000, 2700, "Lymhurst", 0)
Craft_Adepts_Soldier_Boots = CraftingSlot(1, "Adept's Soldier Boots", 8, "Steel Bar")


def calculadora(item):
    # Lista para armazenar os resultados
    resultados = []

    # Inicializar o preço de crafting como infinito
    menor_preco_crafting = float('inf')
    preco_total_crafting = float('inf')

    # Iterando sobre cada instância de CraftingSlot
    for slot in CraftingSlot.instances:
        # Verificando se o nome do item corresponde ao fornecido como entrada
        if slot.item_destino_nome == item.nome:
            resultados.append(slot)

            # Encontrando o item de origem correspondente
            for source_item in Item.instances:
                if source_item.nome == slot.item_source_nome:
                    # Calculando o preço de crafting total
                    preco_total_crafting = source_item.preco_craft * slot.qtd
                    # Verificando se o preço de crafting é menor do que o menor preço de crafting encontrado até agora
                    if preco_total_crafting < menor_preco_crafting:
                        menor_preco_crafting = preco_total_crafting

    # Atualizar o preço de crafting do item com o menor preço encontrado
    item.preco_craft = preco_total_crafting

    # Return não é necessário pois esta é uma função de update, só para visualização
    return resultados, item.preco_craft

# Exemplo de uso
resultado, novo_preco_craft = calculadora(Adepts_Soldier_Boots)
for slot in resultado:
    print("Crafting Slot - ID:", slot.craft_id)
    print("Item Destino:", slot.item_destino_nome)
    print("Quantidade:", slot.qtd)
    print("Item Source:", slot.item_source_nome)

print("Novo preço atualizado para preco_craft:", novo_preco_craft)
