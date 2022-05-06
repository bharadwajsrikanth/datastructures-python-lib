from datastructures.binarysearchtree.binarysearchtree import BinarySearchTree


def test_binarysearchtree_insert_node():
    bst = BinarySearchTree(10)
    bst.insert_node(5)
    bst.insert_node(20)
    assert 10 == bst.get_root().get_val()


def test_binarysearchtree_has_node():
    bst = BinarySearchTree(10)
    bst.insert_node(5)
    bst.insert_node(20)
    if bst.has_key(20):
        assert True


def test_binarysearchtree_does_not_have_node():
    bst = BinarySearchTree(10)
    bst.insert_node(5)
    bst.insert_node(20)
    if not bst.has_key(30):
        assert True

