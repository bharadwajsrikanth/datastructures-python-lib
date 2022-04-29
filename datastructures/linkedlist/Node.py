class Node:
    def __init__(self, val=None, nxt=None):
        self._val = val
        self._next = nxt

    def set_val(self, val):
        self._val = val

    def get_val(self):
        return self._val

    def set_next(self, node):
        self._next = node

    def get_next(self):
        return self._next
