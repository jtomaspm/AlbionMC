import json


def load_steel_bar_data():
    with open(r'C:\Users\mestr\Documents\AlbionMC\CalcAlbion\materials\steel_bar.json', 'r') as file:
        return json.load(file)


def load_ore_data():
    with open(r'C:\Users\mestr\Documents\AlbionMC\CalcAlbion\materials\ore_bar.json', 'r') as file:
        return json.load(file)


class SteelBar:
    def __init__(self, tier=None, city="Martlock", enchantment=None):
        self.tier = tier
        self.city = city
        self.enchantment = enchantment
        self.steel_bar_data = load_steel_bar_data()
        self.ore_data = load_ore_data()
        self.item_value = self.get_item_value()
        self.price = self.get_price(self.steel_bar_data, "steel_bar")
        self.ore_price = self.get_price(self.ore_data, "ore")

    def get_price(self, materials, item_type):
        # print(materials)
        # print(item_type)
        for item in materials[item_type]:
            if (
                    item["tier"] == self.tier
                    and item["city"] == self.city
                    and (item.get("enchantment") == self.enchantment or item.get("enchantment") is None and self.enchantment is None)
            ):
                return item["price"]
        print(f"[WARN] Preço não encontrado para {item_type} T{self.tier} Enc{self.enchantment or 0} em {self.city}")
        return None

    def calc_refine_cost(self):
        if self.tier == 2:
            # Tier 2 SEM enchantment sempre
            return self.ore_price
        elif self.tier == 3:
            ore = self.ore_price
            # Tier 2 SEM enchantment, mesmo que self.enchantment seja diferente
            steel_t2 = SteelBar(2, self.city, enchantment=None)
            return 2 * ore + steel_t2.calc_refine_cost()
        elif self.tier == 4:
            ore = self.ore_price
            # Se o tier 4 TEM enchantment, o tier 3 continua SEM enchantment
            steel_t3 = SteelBar(3, self.city, enchantment=None)
            return 3 * ore + steel_t3.calc_refine_cost()
        return None

    def get_item_value(self, tier=None, enchantment=None, city=None):
        tier = tier or self.tier
        enchantment = enchantment if enchantment is not None else self.enchantment
        city = city or self.city

        for item in self.steel_bar_data["steel_bar"]:
            if item["tier"] == tier and item["city"] == city:
                if ((item.get("enchantment") is None and enchantment is None) or
                        (item.get("enchantment") == enchantment)):
                    return item.get("item_value")
        return None

    def get_production_bonus(self, city=None):
        city = city or self.city
        for entry in self.steel_bar_data.get("refining", []):
            if entry["city"] == city:
                return entry.get("production_bonus")
        return None

    def get_tax_fee(self, city=None):
        city = city or self.city
        for entry in self.steel_bar_data.get("refining", []):
            if entry["city"] == city:
                return entry.get("tax_fee")
        return None

    def calculate_usage_fee(self, tier=None, enchantment=None, city=None):
        """
            Calcula Usage Fee para a cidade passada (default é self.city)
            Formula: ((ItemValue x 0.1125) x TaxFee) / 100
        """
        city = city or self.city
        item_value = self.get_item_value(tier, enchantment, city)
        tax_fee = None
        for entry in self.steel_bar_data.get("refining", []):
            if entry["city"] == city:
                tax_fee = entry.get("tax_fee")
                break
        if item_value is None or tax_fee is None:
            return 0
        return ((item_value * 0.1125) * tax_fee) / 100

    def calculate_resource_return_rate(self, city=None):
        """
            Calcula Resource Return Rate para a cidade passada (default self.city)
            Formula: 1 - 1 / (1 + (ProductionBonus/100))
        """
        city = city or self.city
        production_bonus = self.get_production_bonus(city)

        if production_bonus is None:
            return None

        return (1 - 1 / (1 + production_bonus / 100))

    @staticmethod
    def get_all_refine_paths(tier, city="Martlock", enchantment=None):
        print("tier")
        print(tier)
        print("enchantment")
        print(enchantment)

        def get_steel(t):
            return SteelBar(t, city, enchantment)

        def ore_cost(t):
            print("get_steel(t).ore_price",get_steel(t).ore_price)
            return get_steel(t).ore_price

        def bar_market(t):
            return get_steel(t).price

        def bar_refine(t):
            return get_steel(t).calc_refine_cost()

        def usage_fee(t):
            return get_steel(t).calculate_usage_fee()

        def get_production_bonus(city):
            for entry in SteelBar(1, city).steel_bar_data.get("refining", []):
                if entry["city"] == city:
                    return entry.get("production_bonus", 0)
            return 0

        def calculate_resource_return_rate(city):
            pb = get_production_bonus(city)
            return 1 - 1 / (1 + pb / 100) + 1

        return_rate = calculate_resource_return_rate(city)

        def generate_paths_tier_2():
            custo_sem_uf = ore_cost(2)
            uf = usage_fee(2)
            custo_total = custo_sem_uf * return_rate
            return [{
                "descricao": f"Refinar T2 (enc {enchantment or 0}) com 1x Ore",
                "custo_total": custo_total
            }]

        def generate_paths_tier_3():
            ore_t3 = ore_cost(3)
            steel_t2_ref = bar_refine(2)
            steel_t2_market = bar_market(2)
            steel_t3_market = bar_market(3)
            uf = usage_fee(3)

            return [
                {
                    "descricao": f"Refinar T3 (enc {enchantment or 0}) com 2x Ore + Refino T2",
                    "custo_total": (2 * ore_t3 + steel_t2_ref) * return_rate + uf
                },
                {
                    "descricao": f"Refinar T3 (enc {enchantment or 0}) com 2x Ore + Comprar Steel T2",
                    "custo_total": (2 * ore_t3 + steel_t2_market) * return_rate + uf
                },
                {
                    "descricao": f"Comprar Steel T3 (enc {enchantment or 0}) diretamente",
                    "custo_total": steel_t3_market
                }
            ]

        def generate_paths_tier_4():
            try:
                ore_t4 = ore_cost(4)
                ore_t3 = ore_cost(3)
                steel_t3_ref = bar_refine(3)
                steel_t3_market = bar_market(3)
                steel_t2_market = bar_market(2)
                steel_t4_market = bar_market(4)
                uf = usage_fee(4)

                print("steel_t3_ref =", steel_t3_ref)
                print("steel_t3_market =", steel_t3_market)
                print("steel_t2_market =", steel_t2_market)
                print("steel_t4_market =", steel_t4_market)
                print("uf =", uf)

                return [
                    {
                        "descricao": f"Refinar T4 (enc {enchantment or 0}) com 2x Ore T4 + Refino completo T3",
                        "custo_total": (2 * ore_t4 + steel_t3_ref) * return_rate + uf
                    },
                    {
                        "descricao": f"Refinar T4 (enc {enchantment or 0}) com 2x Ore T4 + Comprar Steel T3",
                        "custo_total": (2 * ore_t4 + steel_t3_market) * return_rate + uf
                    },
                    {
                        "descricao": f"Refinar T4 (enc {enchantment or 0}) com 2x Ore T4 + Refino T3 com Steel T2 comprada",
                        "custo_total": (2 * ore_t4 + (2 * ore_t3 + steel_t2_market)) * return_rate + uf
                    },
                    {
                        "descricao": f"Comprar Steel T4 (enc {enchantment or 0}) diretamente",
                        "custo_total": steel_t4_market
                    }
                ]
            except Exception as e:
                print("error ", e)

        def generate_paths_tier_4_1():
            try:
                ore_t4 = ore_cost(4)
                print("ore_t4 =", ore_t4)

                ore_t3 = ore_cost(3)
                print("ore_t3 =", ore_t3)

                steel_t3_ref = bar_refine(3)
                steel_t3_market = bar_market(3)
                steel_t2_market = bar_market(2)
                steel_t4_market = bar_market(4)
                uf = usage_fee(4)
                print("steel_t3_ref =", steel_t3_ref)
                print("steel_t3_market =", steel_t3_market)
                print("steel_t2_market =", steel_t2_market)
                print("steel_t4_market =", steel_t4_market)
                print("uf =", uf)
                print(ore_t4)
            except Exception as e:
                print("error", e)

        # Encaminhamento com suporte a encantamento
        if tier == 2 and enchantment is None:
            return generate_paths_tier_2()
        elif tier == 3 and enchantment in None:
            return generate_paths_tier_3()
        elif tier == 4 and enchantment is None:
            print("4")
            return generate_paths_tier_4()
        elif tier == 4 and enchantment == 1:
            print("4_1")
            generate_paths_tier_4_1()
            return [{"descricao": "Refino T4.1 ainda não implementado", "custo_total": 0}]
        else:
            return [{"descricao": f"Tier {tier} com enchant {enchantment} ainda não suportado", "custo_total": 0}]
