from AlbionMC_game.craft.item import Item

class Node:
    def __init__(self, value: Item):
        self.value = value
        self.children = [] # type: list[Node]

    def add_child(self, child: 'Node'):
        self.children.append(child)

    def __repr__(self):
        return f"Node(value={self.value}, children={self.children})"

    def __str__(self):
        return f"Node(value={self.value})"