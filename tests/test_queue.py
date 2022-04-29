from datastructures.queue import Queue


def test_queue_enqueue():
    test_queue = Queue()
    test_queue.enqueue(0)
    test_queue.enqueue(1)
    assert test_queue.get_rear_item() == 1


def test_queue_dequeue():
    test_queue = Queue()
    test_queue.enqueue(0)
    test_queue.enqueue(1)
    assert test_queue.dequeue() == 0