from src.lab10.structures import Stack, Queue

def test_stack():
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('C')
    print()
    print("Текущее состояние:", s)

    print("peek():", s.peek())
    print("pop():", s.pop())
    print("После pop:", s)

    print("is_empty:", s.is_empty())
    print("len(stack) =", len(s))


def test_queue():
    q = Queue()
    q.enqueue('A')
    q.enqueue('B')
    q.enqueue('C')
    print()
    print("Текущее состояние:", q)

    print("peek():", q.peek())
    print("dequeue():", q.dequeue())
    print("После dequeue:", q)

    print("is_empty:", q.is_empty())
    print("len(queue) =", len(q))