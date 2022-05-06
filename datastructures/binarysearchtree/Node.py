class Node:
    def __init__(self, val=None, left=None, right=None):
        self._left = left
        self._right = right
        self._val = val

    def set_val(self, val):
        self._val = val

    def get_val(self):
        return self._val

    def set_left(self, node):
        self._left = node

    def get_left(self):
        return self._left

    def set_right(self, node):
        self._right = node

    def get_right(self):
        return self._right
    