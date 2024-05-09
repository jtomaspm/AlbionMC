from colorama import Fore, Style
from ...core.item import Item_OLD
from ...core.crafting_slot import CraftingSlot

def update_crafting_price(item):
    if item.preco_craft == 0:
        return item.preco_mercado

    print(Fore.GREEN, "Item.nome", item.nome, Style.RESET_ALL)

    preco_craft = 0

    # Primeiro, iterar sobre cada instância de Item
    for item_choose in Item_OLD.instances:
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