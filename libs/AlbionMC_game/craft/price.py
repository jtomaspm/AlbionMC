class Price:
    def __init__(self, buy_order: int | None = None, instant_buy: int | None = None):
        self.buy_order = buy_order
        self.instant_buy = instant_buy

    def __str__(self):
        return f"{self.buy_order} silver, {self.instant_buy} gold"

    def __repr__(self):
        return f"Price(silver={self.buy_order}, gold={self.instant_buy})"

    def __eq__(self, other):
        if isinstance(other, Price):
            return self.buy_order == other.buy_order and self.instant_buy == other.instant_buy
        return False