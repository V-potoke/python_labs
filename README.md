# python_labs

## Лабораторная работа 1

### Задание номер 1
```python
name = input('Имя: ')
age = int(input('Возраст: '))
print(f'Привет, {name}! Через год тебе будет {age + 1}.')
```
![Картинка 1](./images/lab01/img01.png)

### Заданиет номер 2
```python
num1 = float(input('a: ').replace(',', '.'))
num2 = float(input('b: ').replace(',', '.'))
print(f'sum={num1 + num2}; avg={round(((num1 + num2) / 2), 2)}')
```
![Картинка 2](./images/lab01/img02.png)

### Задание номер 3
```python
price, discount, vat = float(input('Цена (₽): ')), float(input('Скидка (%): ')), float(input('НДС (%): '))
base = price * (1 - discount / 100)
vat_amount = base * (vat / 100)
total = base + vat_amount
print(f'База после скидки: {format(base, ".2f")} ₽')
print(f'НДС: {format(vat_amount, ".2f")} ₽')
print(f'Итого к оплате: {format(total, ".2f")} ₽')
```
![Картинка 3](./images/lab01/img03.png)

### Задание номер 4
```python
m = int(input('Минуты: '))
hours = (m // 60) % 24
minn = m % 60
if minn < 10:
    minn = '0' + str(minn)
print(f'{hours}:{minn}')
```
![Картинка 4](./images/lab01/img04.png)

### Задание номер 5
```python
a = input('ФИО: ').split()
print(f'Инициалы: {a[0][0] + a[1][0] + a[2][0]}.')
print(f'Длина (символов): {len(a[0]) + len(a[1]) + len(a[2]) + 2}')
```
![Картинка 5](./images/lab01/img05.png)

## Задание номер 6
```python
n = int(input('Пришло людей: '))
ochno, zaochno = 0, 0
for i in range(n):
    inf = input().split()
    if inf[3] == 'True':
        ochno += 1
    else:
        zaochno += 1
print(ochno, zaochno)
```
![Картинка 6](./images/lab01/img06.png)



## Лабораторная работа 2

### Задание номер 1
``` python
def min_max(a):
    if not a:
        return ValueError
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
        return TypeError
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
```
![Картинка 01](./images/lab02/img01.png)

### Задание номер 2
``` python
def transpose(a):
    if a == []:
        return []
    if len(set(len(a1) for a1 in a)) != 1:
        return ValueError
    a_res = []
    for i in range(len(a[0])):
        new_list = []
        for k in range(len(a)):
            new_list.append(a[k][i])
        a_res.append(new_list)
    return a_res


def row_sums(a):
    if len(set(len(a1) for a1 in a)) != 1:
        return ValueError
    return [sum(a1) for a1 in a]


def col_sums(a):
    if a == []:
        return []
    if len(set(len(a1) for a1 in a)) != 1:
        return ValueError
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
```
![Картинка 02](./images/lab02/img02.png)

### Задание номер 3
``` python
def format_record(t):
    fio, group, gpa = t[0].strip(), t[1].strip(), round(t[2], 2)
    if not (len(fio.split()) == 2 or len(fio.split()) == 3) or group == '':
        return ValueError
    if not isinstance(gpa, float):
        return TypeError
    if len(fio.split()) == 3:
        l1, l2 = fio.split()[1], fio.split()[2]
        return fio.split()[0].capitalize() + ' ' + l1[0].upper() + '. ' + l2[0].upper() + '., гр. ' + group + ', GPA ' + f'{gpa:.2f}'
    else:
        l1 = fio.split()[1]
        return fio.split()[0].capitalize() + ' ' + l1[0].upper() + '., гр. ' + group + ', GPA ' + f'{gpa:.2f}'


print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```
![Картинка 03](./images/lab02/img03.png)



## Лабораторная работа 3

### Задание номер A
``` python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True):
    if casefold: text = text.casefold()
    if yo2e: text = text.replace('Ё', 'Е').replace('ё', 'е')
    text = text.replace('\t', ' ').replace('\r', ' ').replace('\n', ' ').strip()
    while '  ' in text: text = text.replace('  ', ' ')
    return text


def tokenize(text):
    return re.findall(r'\w+[-]\w+|\w+', text.lower())


def count_freq(tokens):
    t = {}
    while tokens:
        t[tokens[0]] = tokens.count(tokens[0])
        tokens = [x for x in tokens if x != tokens[0]]
    return t


def top_n(freq, n):
    top_n = []
    freq = sorted(freq.items(), key=lambda item: [-item[1], item[0]])
    for i in range(min(n, len(freq))):
        top_n.append(freq[i])
    return top_n
```
![Картинка 01](./images/lab03/A.png)

### Задание номер B
``` python
NICE_CONCLUSION = True
text = sys.stdin.read()
text = normalize(text)
tokens = tokenize(text)
top = top_n(count_freq(tokens), len(tokens))
print(f'Всего слов: {len(tokens)}')
print(f'Уникальных слов: {len(set(tokens))}')
print('Топ-5:')
if NICE_CONCLUSION:
    mx_len = max(5, len(max(tokens, key=len)))
    print('слово' + ' ' * (mx_len - 5) + ' | ' + 'частота')
    print('-' * (mx_len + 10))
    for i in top:
        print(i[0] + ' ' * (mx_len - len(i[0])) + ' | ' + str(i[1]))
else:
    for i in top:
        print(f'{i[0]}:{i[1]}')
```
![Картинка 02](./images/lab03/B.png)
