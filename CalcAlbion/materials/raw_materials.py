import json


def load_steel_bar_data():
    with open(r'C:\Users\mestr\Documents\AlbionMC\CalcAlbion\materials\steel_bar.json', 'r') as file:
        return json.load(file)


def load_ore_data():
    with open(r'C:\Users\mestr\Documents\AlbionMC\CalcAlbion\materials\ore_bar.json', 'r') as file:
        return json.load(file)


class SteelBar:
    def __init__(self, tier, city="Martlock"):
        self.tier = tier
        self.city = city

        self.steel_bar_data = load_steel_bar_data()
        self.ore_data = load_ore_data()

        self.price = self.get_price(self.steel_bar_data, "steel_bar")
        self.ore_price = self.get_price(self.ore_data, "ore")

    def get_price(self, materials, item_type):
        for item in materials[item_type]:
            if item["tier"] == self.tier and item["city"] == self.city:
                return item["price"]
        return None

    def calc_refine_cost(self):
        if self.tier == 2:
            return self.ore_price
        elif self.tier == 3:
            ore = self.ore_price
            steel_t2 = SteelBar(2, self.city)
            return 2 * ore + steel_t2.calc_refine_cost()
        elif self.tier == 4:
            ore = self.ore_price
            steel_t3 = SteelBar(3, self.city)
            return 3 * ore + steel_t3.calc_refine_cost()
        return None

    @staticmethod
    def get_all_refine_paths(tier, city="Martlock"):
        def get_steel(t): return SteelBar(t, city)
        def ore_cost(t): return get_steel(t).ore_price
        def bar_market(t): return get_steel(t).price
        def bar_refine(t): return get_steel(t).calc_refine_cost()

        def generate_paths_tier_2():
            return [{
                "descricao": "Refinar T2 com 1x Ore T2",
                "custo_total": ore_cost(2)
            }]

        def generate_paths_tier_3():
            ore = ore_cost(3)
            steel_t2_ref = bar_refine(2)
            steel_t2_market = bar_market(2)
            steel_t3_market = bar_market(3)

            return [
                {
                    "descricao": "Refinar T3 com 2x Ore T3 + Refino T2",
                    "custo_total": 2 * ore + steel_t2_ref
                },
                {
                    "descricao": "Refinar T3 com 2x Ore T3 + Comprar Steel Bar T2",
                    "custo_total": 2 * ore + steel_t2_market
                },
                {
                    "descricao": "Comprar Steel Bar T3 diretamente",
                    "custo_total": steel_t3_market
                }
            ]

        def generate_paths_tier_4():
            ore = ore_cost(4)
            ore_t3 = ore_cost(3)
            steel_t3_ref = bar_refine(3)
            steel_t3_market = bar_market(3)
            steel_t2_market = bar_market(2)
            steel_t4_market = bar_market(4)

            return [
                {
                    "descricao": "Refinar T4 com 3x Ore T4 + Refino completo T3",
                    "custo_total": 3 * ore + steel_t3_ref
                },
                {
                    "descricao": "Refinar T4 com 3x Ore T4 + Comprar Steel Bar T3",
                    "custo_total": 3 * ore + steel_t3_market
                },
                {
                    "descricao": "Refinar T4 com 3x Ore T4 + Refino T3 com Steel Bar T2 comprada",
                    "custo_total": 3 * ore + (2 * ore_t3 + steel_t2_market)
                },
                {
                    "descricao": "Comprar Steel Bar T4 diretamente",
                    "custo_total": steel_t4_market
                }
            ]

        if tier == 2:
            return generate_paths_tier_2()
        elif tier == 3:
            return generate_paths_tier_3()
        elif tier == 4:
            return generate_paths_tier_4()
        else:
            return [{"descricao": f"Tier {tier} ainda não suportado", "custo_total": 0}]
