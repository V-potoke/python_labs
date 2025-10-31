def transpose(a):
    if a == []:
        return []
    if len(set(len(a1) for a1 in a)) != 1:
        raise ValueError('Рваная матрица')
    a_res = []
    for i in range(len(a[0])):
        new_list = []
        for k in range(len(a)):
            new_list.append(a[k][i])
        a_res.append(new_list)
    return a_res


def row_sums(a):
    if len(set(len(a1) for a1 in a)) != 1:
        raise ValueError('Рваная матрица')
    return [sum(a1) for a1 in a]


def col_sums(a):
    if a == []:
        return []
    if len(set(len(a1) for a1 in a)) != 1:
        raise ValueError('Рваная матрица')
    a_res = []
    for i in range(len(a[0])):
        new_list = []
        for k in range(len(a)):
            new_list.append(a[k][i])
        a_res.append(new_list)
    return [sum(a1) for a1 in a_res]


print('transpose')
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))

print('row_sums')
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))

print('col_sums')
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
