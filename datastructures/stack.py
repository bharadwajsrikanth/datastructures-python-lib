class Stack:
    def __init__(self):
        self._elements = []

    def push(self, value):
        self._elements.append(value)

    def pop(self):
        if self.is_empty():
            raise Exception("Popping from an empty stack is not permitted")
        value = self._elements.pop(len(self._elements) - 1)
        return value

    def peek(self):
        if self.is_empty():
            raise Exception("Peeking from an empty stack is not permitted")
        return self._elements[len(self._elements) - 1]

    def get_size(self):
        return len(self._elements)

    def is_empty(self):
        return len(self._elements) == 0
