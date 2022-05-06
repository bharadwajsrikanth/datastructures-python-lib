from datastructures.binarysearchtree.Node import Node


class BinarySearchTree:
    def __init__(self, key=None):
        self._root = Node(key)

    def set_root(self, root):
        self._root = root

    def get_root(self):
        return self._root

    def insert_node(self, key):
        new_node = Node(key)
        if self.get_root() is None:
            self.set_root(new_node)

        temp_root = self.get_root()
        parent = None

        while temp_root is not None:
            parent = temp_root
            if key < temp_root.get_val():
                temp_root = temp_root.get_left()
            else:
                temp_root = temp_root.get_right()

        if key < parent.get_val():
            parent.set_left(new_node)
        else:
            parent.set_right(new_node)
            
