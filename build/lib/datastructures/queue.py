class Queue:
    def __init__(self):
        self._elements = []

    def enqueue(self, value):
        self._elements.append(value)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Removing from an empty queue is not permitted")
        value = self._elements.pop(0)
        return value

    def get_size(self):
        return len(self._elements)

    def is_empty(self):
        return len(self._elements) == 0

    def get_front_item(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._elements[0]

    def get_rear_item(self):
        if self.is_empty():
            raise Exception("Queue is empty")
        return self._elements[len(self._elements) - 1]

