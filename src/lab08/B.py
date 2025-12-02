from models import Student
from src.lab08.serialize import students_to_json, students_from_json


stud = [
    Student("Иванов Иван Иванович", "2007-01-15", "БИВТ-25-1", 4.5),
    Student("Петрова Анна Сергеевна", "2007-03-22", "БИВТ-25-2", 4.8),
    Student("Сидоров Алексей Петрович", "2007-05-10", "БИВТ-25-3", 3.9),
    Student("Козлова Мария Владимировна", "2007-07-28", "БИВТ-25-4", 4.2)
]

students_to_json(stud, 'C:/Users/vende/PycharmProjects/python_labs/data/lab08/students_output.json')
print(students_from_json('C:/Users/vende/PycharmProjects/python_labs/data/lab08/students_output.json'))