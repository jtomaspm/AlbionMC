class Path:
    def __init__(self, nodes=None):
        if nodes is None:
            nodes = []
        self.nodes = nodes

    def add_node(self, node):
        self.nodes.append(node)

    def __len__(self):
        return len(self.nodes)

    def __getitem__(self, index):
        return self.nodes[index]

    def __iter__(self):
        return iter(self.nodes)

    def __str__(self):
        return " -> ".join(str(node) for node in self.nodes)

    def __repr__(self):
        return f"Path({self.nodes})"