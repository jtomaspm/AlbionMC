from colorama import Fore, Style

from backend.core.Item import Item, CraftingSlot

# Materiais_item
Steel_Bar = Item("Steel Bar", 270, 400, "Lymhurst", 0)
Bronze_Bar = Item("Bronze Bar", 100, 90, "Lymhurst", 0)
Copper_Bar = Item("Copper Bar", 60, 55, "Lymhurst", 0)

# Materiais_craft
Craft_Steel_Bar = CraftingSlot(1, "Steel_Bar", 2, "Bronze Bar")
Craft_Steel_Bar2 = CraftingSlot(1, "Steel_Bar", 1, "Copper Bar")

# Items_item
Adepts_Soldier_Boots = Item("Adept's Soldier Boots", 3000, 2700, "Lymhurst", 0)

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
                        print(Fore.GREEN, f'O Item {source_item.nome} é mais barato craftar que comprar. Preço para craftar: {source_item.preco_craft}', Style.RESET_ALL)
                        preco_total_crafting = source_item.preco_craft * slot.qtd
                    else:
                        print(Fore.GREEN, f'O Item {source_item.nome} é mais barato comprar que craftar. Preço para comprar: {source_item.preco_mercado}', Style.RESET_ALL)
                        preco_total_crafting = source_item.preco_mercado * slot.qtd

    return resultados, preco_total_crafting

# Exemplo de uso
resultado, novo_preco_craft = calculadora(Adepts_Soldier_Boots)
for slot in resultado:
    print("Crafting Slot - ID:", slot.craft_id)
    print("Item Destino:", slot.item_destino_nome)
    print("Quantidade:", slot.qtd)
    print("Item Source:", slot.item_source_nome)

print("Novo preço atualizado para preco_craft:", novo_preco_craft)
