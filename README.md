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
