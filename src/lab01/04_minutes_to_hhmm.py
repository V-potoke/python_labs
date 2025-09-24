m = int(input('Минуты: '))
hours = (m // 60) % 24
minn = m % 60
if minn < 10:
    minn = '0' + str(minn)
print(f'{hours}:{minn}')
