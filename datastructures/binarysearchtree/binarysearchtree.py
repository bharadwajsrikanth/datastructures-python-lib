from datastructures.binarysearchtree.Node import Node


class BinarySearchTree:
    def __init__(self, key=None):
        self._root = Node(key)

    def _search_node(self, key):
        temp_root = self.get_root()

        while temp_root is not None:
            if key > temp_root.get_val():
                temp_root = temp_root.get_right()
            elif key < temp_root.get_val():
                temp_root = temp_root.get_left()
            else:
                return temp_root

        return None

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

    def has_key(self, key):
        return self._search_node(key) is not None

    def delete_node(self, key):
        temp_root = self.get_root()
        parent = None

        while temp_root is not None and temp_root.get_val() != key:
            parent = temp_root
            if temp_root.get_val() > key:
                temp_root = temp_root.get_left()
            else:
                temp_root = temp_root.get_right()

        if temp_root is None:
            raise Exception("The given key is not found in the tree")

        if temp_root.get_left() is None or temp_root.get_right() is None:
            cur = None
            if temp_root.get_left() is None:
                cur = temp_root.get_right()
            else:
                cur = temp_root.get_right()

            if parent is None:
                self.set_root(cur)

            if temp_root == parent.get_left():
                parent.set_left(cur)
            else:
                parent.set_right(cur)

            temp_root = None

        else:
            parent = None
            cur = None

            cur = temp_root.get_right()
            while cur.get_left() is not None:
                parent = cur
                cur = cur.get_left()

            if parent is not None:
                parent.set_left(cur.get_right())

            else:
                temp_root.set_right(cur.get_right())

            temp_root.set_val(cur.get_val())
            cur = None

