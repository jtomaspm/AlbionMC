from colorama import Fore, Style

from backend.core.Item import Item, CraftingSlot

# Materiais_item
Steel_Bar = Item("Steel Bar", 750, 400, "Lymhurst", 0)
Iron_Ore = Item("Iron Ore", 270, 0, "Lymhurst", 0)
Bronze_Bar = Item("Bronze Bar", 60, 90, "Lymhurst", 0)
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

                if preco_craft_material > item_choose.preco_mercado:
                    preco_craft_material = item_choose.preco_mercado

                # Verificar se o preço do material foi atualizado com sucesso
                try:
                    preco_craft += preco_craft_material * craftingSlot.qtd
                except Exception as e:
                    print(Fore.LIGHTRED_EX, f" Erro no cálculo do preço - Exception Rised {e} - ", Style.RESET_ALL)

    print(Fore.CYAN, "item.nome", item.nome, "novo preço do craft", preco_craft, Style.RESET_ALL)
    item.preco_craft = preco_craft
    return item.preco_craft  # Retornar o preço de crafting do item atualizado

def selector(item):
    preco_craft = update_crafting_price(item)

    mensagem = "Informações para {}\n".format(item.nome)
    mensagem += "Preço do item: {}\n".format(item.preco_mercado)
    mensagem += "Preço de crafting: {}\n".format(preco_craft)

    # Verificar se o preço de crafting é menor do que o preço de mercado
    if preco_craft < item.preco_mercado:
        return f"Preço de crafting ({preco_craft}) é mais barato do que o preço de mercado ({item.preco_mercado}) para {item.nome}"
    elif preco_craft > item.preco_mercado:
        return f"Preço de mercado ({item.preco_mercado}) é mais barato do que o preço de crafting ({preco_craft}) para {item.nome}"
    else:
        return f"Preços de crafting ({preco_craft}) e mercado ({item.preco_mercado}) são iguais para {item.nome}"


# [Zona de testes]
# update_crafting_price(Adepts_Soldier_Boots)
# update_crafting_price(Steel_Bar)
# print("Preço de crafting atualizado para Adepts_Soldier_Boots:", Adepts_Soldier_Boots.preco_craft)
# print("Preço de crafting atualizado para Steel_Bar:", Steel_Bar.preco_craft)
print(Fore.MAGENTA, selector(Adepts_Soldier_Boots), Style.RESET_ALL)
