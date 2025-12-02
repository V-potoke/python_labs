from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


json_to_csv('C:/Users/vende/PycharmProjects/python_labs/data/samples/people.json', 'C:/Users/vende/PycharmProjects/python_labs/data/out/people.csv')
csv_to_json('C:/Users/vende/PycharmProjects/python_labs/data/samples/people.csv', 'C:/Users/vende/PycharmProjects/python_labs/data/out/people.json')
csv_to_xlsx('C:/Users/vende/PycharmProjects/python_labs/data/samples/cities.csv', 'C:/Users/vende/PycharmProjects/python_labs/data/out/cities.xlsx')
