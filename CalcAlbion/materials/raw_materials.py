import json

def load_steel_bar_data():
    with open('steel_bar.json', 'r') as file:
        steel_bar_data = json.load(file)
    return steel_bar_data

def load_ore_data():
    with open('ore.json', 'r') as file:
        ore_data = json.load(file)
    return ore_data


class SteelBar:
    def __int__(self):
        self.price = None
        self.tier = None
        self.city = None
        self.enchantment = None
        self.steel_bar_json = load_steel_bar_data()
        self.ore_json = load_ore_data()

    def get_price(self, materials, item_type, tier, city="Martlock"):
        for item in materials[item_type]:
            if item["tier"] == tier and item["city"] == city:
                return item["price"]
        return None

    def calc_refine_cost(self, tier, city="Martlock"):
        if tier == 2:
            ore_price = self.get_price(self.ore_json, "ore", 2, city)
            return ore_price

        elif tier == 3:
            ore_price = self.get_price(self.ore_json, "ore", 3, city)
            bar_t2_price = self.calc_refine_cost(2, city)
            return 2 * ore_price + 1 * bar_t2_price

        elif tier == 4:
            ore_price = self.get_price(self.ore_json, "ore", 4, city)
            bar_t3_price = self.calc_refine_cost(3, city)
            return 3 * ore_price + 1 * bar_t3_price

        else:
            return None