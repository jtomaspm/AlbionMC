from AlbionMC_game.craft.item import Item

class Node:
    def __init__(self, value: Item, quantity: int = 1):
        if quantity < 1:
            raise ValueError("Quantity must be at least 1")
        self.value = value
        self.quantity = quantity
        self.children = [] # type: list[Node]

    def add_child(self, child: 'Node'):
        self.children.append(child)

    def __repr__(self):
        return f"Node(value={self.value}, children={self.children})"

    def __str__(self):
        return f"Node(value={self.value})"