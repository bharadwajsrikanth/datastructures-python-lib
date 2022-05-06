from datastructures.binarysearchtree.binarysearchtree import BinarySearchTree


def test_binarysearchtree_insert_node():
    bst = BinarySearchTree(10)
    bst.insert_node(5)
    bst.insert_node(20)
    assert 10 == bst.get_root().get_val()
