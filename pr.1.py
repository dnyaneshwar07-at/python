class Node:
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def display(self, level=0):
        print("  " * level + self.name)
        for child in self.children:
            child.display(level + 1)

# Example hierarchy
root = Node("Company")

hr = Node("HR")
it = Node("IT")

root.add_child(hr)
root.add_child(it)

it.add_child(Node("Development"))
it.add_child(Node("Support"))

root.display()