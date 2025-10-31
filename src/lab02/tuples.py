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
