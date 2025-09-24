n = int(input('Пришло людей: '))
ochno, zaochno = 0, 0
for i in range(n):
    inf = input().split()
    if inf[3] == 'True':
        ochno += 1
    else:
        zaochno += 1
print(ochno, zaochno)
