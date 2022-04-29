from datastructures.stack import Stack


def test_stack_push():
    test_stack = Stack()
    test_stack.push(0)
    test_stack.push(1)
    assert test_stack.peek() == 1


def test_stack_pop():
    test_stack = Stack()
    test_stack.push(0)
    test_stack.push(1)
    assert test_stack.pop() == 1
