from abc import ABC, abstractmethod

from AlbionMC_game.craft.tree import Tree
from AlbionMC_game.craft.node import Node
from AlbionMC_game.craft.price import Price

class SearchStrategy(ABC):
    def __init__(self, tree: Tree):
        self.tree = tree

    @abstractmethod
    def next(self, *args, **kwargs) -> Node | None:
        pass

class InstantBuyIfLessThanXPercentAboveBuyOrder(SearchStrategy):
    def next(self, *args) -> Node | None:
        if not args:
            raise Exception("Percentage threshold must be provided")
        percentage_threshold = args[0]

        node = self.tree.current
        if not node.children:
            return None

        best = None # type: Node | None
        best_cost = None # type: Price | None
        use_instant_buy_best = False
        for child in node.children:
            cost = child.value.fetch_cost()
            if best is None:
                best = child
                best_cost = cost
                use_instant_buy_best = False
                continue
            if cost is None:
                continue

            use_instant_buy = cost.instant_buy is not None and not (cost.buy_order is not None and cost.instant_buy < cost.buy_order * (1 + percentage_threshold / 100))

            if not use_instant_buy and not cost.buy_order:
                continue 
            if not use_instant_buy_best and (not best_cost or not best_cost.buy_order):
                best = child
                best_cost = cost
                use_instant_buy_best = use_instant_buy
                continue

            if use_instant_buy and use_instant_buy_best and cost.instant_buy is not None and best_cost is not None and best_cost.instant_buy is not None and cost.instant_buy < best_cost.instant_buy:
                best = child
                best_cost = cost
                use_instant_buy_best = use_instant_buy
                continue


        if best_cost is None or best is None:
            return None

        self.tree.current = best
        return best