from datastructures.linkedlist.linkedlist import LinkedList


def test_linkedlist_append():
    ll = LinkedList()
    ll.append_node(10)
    ll.append_node(20)
    assert [10, 20] == ll.traverse()


def test_linkedlist_prepend():
    ll = LinkedList()
    ll.prepend_node(10)
    ll.prepend_node(20)
    assert [20, 10] == ll.traverse()


def test_remove_data():
    ll = LinkedList()
    ll.prepend_node('apple')
    ll.prepend_node('ball')
    ll.prepend_node('cat')
    ll.remove_node('ball')
    assert ['cat', 'apple'] == ll.traverse()
