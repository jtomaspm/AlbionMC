

# Materiais_item
from src.core.item import Item_OLD
from src.core.crafting_slot import CraftingSlot


Steel_Bar = lambda : Item_OLD("Steel Bar", 750, 400, "Lymhurst", 0)
Iron_Ore = lambda : Item_OLD("Iron Ore", 270, 0, "Lymhurst", 0)
Bronze_Bar = lambda : Item_OLD("Bronze Bar", 60, 90, "Lymhurst", 0)
Tin_Ore = lambda : Item_OLD("Tin Ore", 270, 0, "Lymhurst", 0)
Copper_Bar = lambda : Item_OLD("Copper Bar", 60, 55, "Lymhurst", 0)
Copper_Ore = lambda : Item_OLD("Copper Ore", 30, 0, "Lymhurst", 0)

# Materiais_craft
Craft_Steel_Bar = lambda : CraftingSlot(1, "Steel Bar", 2, "Iron Ore")
Craft_Steel_Bar2 = lambda : CraftingSlot(1, "Steel Bar", 1, "Bronze Bar")

Craft_Bronze_Bar = lambda : CraftingSlot(1, "Bronze Bar", 2, "Tin Ore")
Craft_Bronze_Bar2 = lambda : CraftingSlot(1, "Bronze Bar", 1, "Copper Bar")

Craft_Copper_Bar = lambda : CraftingSlot(1, "Copper Bar", 1, "Copper Ore")

# Items_item
Adepts_Soldier_Boots = lambda : Item_OLD("Adept's Soldier Boots", 4000, 2700, "Lymhurst", 0)

# Items_craft
Craft_Adepts_Soldier_Boots = lambda : CraftingSlot(1, "Adept's Soldier Boots", 8, "Steel Bar")