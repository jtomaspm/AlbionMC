from AlbionMC_game.craft.node import Node
from AlbionMC_game.craft.search_strategy import SearchStrategy


class Tree:
    def __init__(self, root: Node, search_strategy: SearchStrategy):
        self.root = root
        self.current = root
        self.children = []
        self.search_strategy = search_strategy

    def add_child(self, child: Node):
        self.children.append(child)
        self.current.add_child(child)

    def __repr__(self):
        return f"Tree(root={self.root}, children={self.children})"

    def __str__(self):
        return f"Tree with root: {self.root} and {len(self.children)} children"