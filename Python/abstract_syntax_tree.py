from node import Node
from graphviz import Digraph

class Abstract_Syntax_Tree:
    def __init__(self, root_node_name):
        self.graph = Digraph('abstract_syntax_tree', filename='abstract_syntax_tree.gv')
        self.root = self.add_node(root_node_name, root_node_name)

    def add_node(self, name, label):
        self.graph.node(name, label)
        node = Node(name, label)
        return node

    def add_child(self, child, parent):
        parent.add_child(child)
        self.graph.edge(parent.get_name(), child.get_name())

    def get_root(self):
        return self.root

    def view_graph(self):
        self.graph.view()