from abc import ABC, abstractmethod
from typing import Optional

from AlbionMC_game.craft.tree import Tree
from AlbionMC_game.craft.node import Node
from AlbionMC_game.craft.price import Price
from AlbionMC_game.craft.path import Path

class SearchStrategy(ABC):
    def __init__(self, tree: Tree):
        self.tree = tree

    @abstractmethod
    def get_cost(self, *args, **kwargs) -> Optional[Path]:
        pass

class InstantBuyIfLessThanXPercentAboveBuyOrder(SearchStrategy):
    def get_cost(self, *args) -> Optional[Node]:
        if not args:
            raise Exception("Percentage threshold must be provided")
        percentage_threshold = args[0]

        node = self.tree.current

        # for each node  get price from market, then sum children get_cost() and compare market price vs crafted price