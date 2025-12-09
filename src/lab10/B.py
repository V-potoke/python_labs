from src.lab10.linked_list import SinglyLinkedList


def test_linked_list():
    lst = SinglyLinkedList()
    lst.append('A')
    lst.append('B')
    lst.append('C')
    print()
    print("Текущее состояние:", lst)

    print("prepend(5)")
    lst.prepend('D')
    print("После prepend:", lst)

    print("insert(2, 99)")
    lst.insert(2, 'E')
    print("После insert:", lst)

    print("remove_at(1)")
    lst.remove_at(1)
    print("После remove_at:", lst)

    print("len(list) =", len(lst))
    print("Элементы списка:", list(lst))