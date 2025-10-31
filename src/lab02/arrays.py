def min_max(a):
    if not a:
        raise ValueError('Пустой список')
    return (min(a), max(a))


def unique_sorted(a):
    return sorted(set(a))


def flatten(a):
    row_major = []
    fl = False
    for a1 in a:
        if not isinstance(a1, (list, tuple)):
            fl = True
            break
        for i in range(len(a1)):
            row_major.append(a1[i])
    if fl:
        raise TypeError('данная/ый строка/элемент не является списком/кортежем')
    return row_major


print('min_max')
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))

print('unique_sorted')
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))

print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
