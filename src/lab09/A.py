from src.lab09.group import Group
from src.lab08.models import Student


def main():
    path = "C:/Users/vende/PycharmProjects/python_labs/data/lab09/students.csv"
    group = Group(path)

    print("СПИСОК ДО ИЗМЕНЕНИЙ:")
    for s in group.list():
        print("  ", s)

    print("ДОБАВЛЕНИЕ СТУДЕНТА")
    new_student = Student(
        fio="Тестовый Студент",
        birthdate="2007-05-01",
        group="БИВТ-25-3",
        gpa=4.6
    )
    group.add(new_student)
    print("   Добавлен:", new_student)

    print("СПИСОК ПОСЛЕ ДОБАВЛЕНИЯ:")
    for s in group.list():
        print("  ", s)

    print("ПОИСК ПО ПОДСТРОКЕ 'Тест'")
    found = group.find("Тест")
    for s in found:
        print("   Найден:", s)

    print("СМЕНА GPA У 'Тестового студента'")
    group.update("Тестовый Студент", gpa=5.0)
    print("   GPA успешно изменён.")

    print("СПИСОК ПОСЛЕ ИЗМЕНЕНИЯ:")
    for s in group.list():
        print("  ", s)

    print("УДАЛЕНИЕ 'Тестового студента'")
    group.remove("Тестовый Студент")
    print("   Тестовый Студент успешно удалён")

    print("СПИСОК ПОСЛЕ ВСЕХ ИЗМЕНЕНИЙ:")
    for s in group.list():
        print("  ", s)


if __name__ == "__main__":
    main()