from datastructures.linkedlist.Node import Node


class LinkedList:
    def __init__(self, node=None):
        self._head = node

    def _set_head(self, node):
        self._head = node

    def _get_head(self):
        return self._head

    def append_node(self, data):
        new_node = Node()
        new_node.set_val(data)
        if not self._get_head():
            self._set_head(new_node)
            return
        cur = self._get_head()
        while cur.get_next():
            cur = cur.get_next()
        cur.set_next(new_node)

    def prepend_node(self, data):
        new_node = Node()
        new_node.set_val(data)
        if not self._get_head():
            self._set_head(new_node)
            return
        cur = self._get_head()
        new_node.set_next(cur)
        self._set_head(new_node)

    def remove_node(self, data):
        if not self._get_head():
            raise Exception("Node cannot be removed from empty list")
        cur = self._get_head()
        if cur.get_val() == data:
            self._set_head(cur.get_next())
            return
        while cur:
            if cur.get_val() == data:
                break
            prev = cur
            cur = cur.get_next()

        if not cur:
            raise Exception("Node with given data is not available in the list")

        prev.set_next(cur.get_next())

    def traverse(self):
        elements = []
        if not self._get_head():
            raise Exception("Empty list cannot be traversed")
        cur = self._get_head()
        while cur:
            elements.append(cur.get_val())
            cur = cur.get_next()
        return elements

    def search(self, data):
        if not self._get_head():
            raise Exception("Empty list cannot be searched")
        cur = self._get_head()
        while cur:
            if cur.get_val() == data:
                return True
        return False




