class Node:
    def __init__(self, name, label):
        self.name = name
        self.label = label
        self.children = []
        self.parent = None

    def set_parent(self, node):
        self.parent = node

    def add_child(self, child):
        self.children.append(child)
        child.set_parent(self)

    def get_name(self):
        return self.name