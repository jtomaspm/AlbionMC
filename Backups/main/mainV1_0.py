from colorama import Fore, Style

from backend.core.Item import Item, CraftingSlot

# Materiais_item
Steel_Bar = Item("Steel Bar", 270, 400, "Lymhurst", 0)
Iron_Ore = Item("Iron Ore", 270, 0, "Lymhurst", 0)
Bronze_Bar = Item("Bronze Bar", 100, 90, "Lymhurst", 0)
Tin_Ore = Item("Tin Ore", 270, 0, "Lymhurst", 0)
Copper_Bar = Item("Copper Bar", 60, 55, "Lymhurst", 0)
Copper_Ore = Item("Copper Ore", 30, 0, "Lymhurst", 0)

# Materiais_craft
Craft_Steel_Bar = CraftingSlot(1, "Steel Bar", 2, "Iron Ore")
Craft_Steel_Bar2 = CraftingSlot(1, "Steel Bar", 1, "Bronze Bar")

Craft_Bronze_Bar = CraftingSlot(1, "Bronze Bar", 2, "Tin Ore")
Craft_Bronze_Bar2 = CraftingSlot(1, "Bronze Bar", 1, "Copper Bar")

Craft_Copper_Bar = CraftingSlot(1, "Copper Bar", 1, "Copper Ore")

# Items_item
Adepts_Soldier_Boots = Item("Adept's Soldier Boots", 4000, 2700, "Lymhurst", 0)

# Items_craft
Craft_Adepts_Soldier_Boots = CraftingSlot(1, "Adept's Soldier Boots", 8, "Steel Bar")


def calculadora(item):
    print(Fore.YELLOW, f'Vamos calcular qual a maneira mais barata de craftar o item {item.nome}', Style.RESET_ALL)
    # Lista Temporária para armazenar os resultados
    resultados = []

    # Inicializar o preço de crafting como infinito
    preco_total_crafting = float('inf')

    # Iterando sobre cada instância de CraftingSlot
    for slot in CraftingSlot.instances:
        # Verificando se o nome do item corresponde ao fornecido como entrada
        if slot.item_destino_nome == item.nome:
            resultados.append(slot)

            # Encontrando o item de origem correspondente
            for source_item in Item.instances:
                if source_item.nome == slot.item_source_nome:
                    if source_item.preco_craft and source_item.preco_craft <= source_item.preco_mercado:
                        print(Fore.GREEN,
                              f'O Item {source_item.nome} é mais barato craftar que comprar. Preço para craftar: {source_item.preco_craft}',
                              Style.RESET_ALL)
                        preco_total_crafting = source_item.preco_craft * slot.qtd
                    else:
                        print(Fore.GREEN,
                              f'O Item {source_item.nome} é mais barato comprar que craftar. Preço para comprar: {source_item.preco_mercado}',
                              Style.RESET_ALL)
                        preco_total_crafting = source_item.preco_mercado * slot.qtd

    return resultados, preco_total_crafting


def selector(item):
    # O return ainda está mal, mas imaginemos que resultados[0] é a recipie e preco_craft o seu valor correto
    resultados, preco_craft = calculadora(Adepts_Soldier_Boots)

    # Se não houver resultados, significa que não há receitas disponíveis
    if not resultados:
        return "Não há receitas disponíveis para {}".format(item.nome)

    # Construir mensagem com informações sobre o item
    mensagem = "Informações para {}\n".format(item.nome)
    mensagem += "Preço do item: {}\n".format(item.preco_mercado)
    mensagem += "Preço de crafting: {}\n".format(preco_craft)

    # Verificar se o preço de crafting é menor do que o preço de mercado
    if preco_craft < item.preco_mercado:
        return "Preço de crafting é mais barato para {}".format(item.nome)
    elif preco_craft > item.preco_mercado:
        return "Preço de mercado é mais barato para {}".format(item.nome)
    else:
        return "Preços de crafting e mercado são iguais para {}".format(item.nome)


# def update_crafting_price(item):
#     if item.preco_craft == 0:
#         return item.preco_mercado
#     print(Fore.GREEN,"Item.nome", item.nome, Style.RESET_ALL)
#     preco_craft = 0
#     # Iterar sobre cada instância de CraftingSlot
#     for craftingSlot in CraftingSlot.instances:
#         # Verificar se o nome do item corresponde ao fornecido como entrada
#         if craftingSlot.item_destino_nome == item.nome:
#             # Iterar sobre cada material necessário para crafting
#             for item_choose in Item.instances:
#                 if item_choose.nome == craftingSlot.item_source_nome:
#                     print(Fore.YELLOW,"slot.item_destino_nome", craftingSlot.item_destino_nome, Style.RESET_ALL)
#                     preco_craft_material = update_crafting_price(item_choose)
#                     print(Fore.RED, "craftingSlot.item_source_nome", item_choose.nome,"preço", preco_craft_material, Style.RESET_ALL)
#                     input("next")
#                     preco_craft += preco_craft_material * craftingSlot.qtd
#
#     item.preco_craft = preco_craft
#
# update_crafting_price(Adepts_Soldier_Boots)
# print("Preço de crafting atualizado para Adepts_Soldier_Boots:", Adepts_Soldier_Boots.preco_craft)
#

def update_crafting_price(item):
    if item.preco_craft == 0:
        return item.preco_mercado

    print(Fore.GREEN, "Item.nome", item.nome, Style.RESET_ALL)

    preco_craft = 0

    # Primeiro, iterar sobre cada instância de Item
    for item_choose in Item.instances:
        # Verificar se há uma receita de crafting que requer este item
        for craftingSlot in CraftingSlot.instances:
            # Verificar se o nome do item corresponde ao fornecido como entrada
            if craftingSlot.item_destino_nome == item.nome and item_choose.nome == craftingSlot.item_source_nome:
                print(Fore.YELLOW, "slot.item_destino_nome", craftingSlot.item_destino_nome, Style.RESET_ALL)

                # Primeiro, atualizar o preço do Item necessário
                preco_craft_material = update_crafting_price(item_choose)
                print(Fore.RED, "craftingSlot.item_source_nome", item_choose.nome, "preço", preco_craft_material,
                      Style.RESET_ALL)
                input("next")

                # Verificar se o preço do material foi atualizado com sucesso
                if preco_craft_material is not None:
                    preco_craft += preco_craft_material * craftingSlot.qtd

    print(Fore.CYAN, "item.nome", item.nome, "novo preço do craft", preco_craft)
    item.preco_craft = preco_craft
    return item.preco_craft  # Retornar o preço de crafting do item atualizado


update_crafting_price(Adepts_Soldier_Boots)
update_crafting_price(Steel_Bar)
print("Preço de crafting atualizado para Adepts_Soldier_Boots:", Adepts_Soldier_Boots.preco_craft)
print("Preço de crafting atualizado para Steel_Bar:", Steel_Bar.preco_craft)

# # Exemplo de uso
# resultado, novo_preco_craft = calculadora(Adepts_Soldier_Boots)
# for slot in resultado:
#     print("Crafting Slot - ID:", slot.craft_id)
#     print("Item Destino:", slot.item_destino_nome)
#     print("Quantidade:", slot.qtd)
#     print("Item Source:", slot.item_source_nome)
#
# print("Novo preço atualizado para preco_craft:", novo_preco_craft)

# print(selector(Adepts_Soldier_Boots))

# Ainda é preciso mudar os retrurns e o caralho para ele devolver a recipie com id = 1 -> preco
