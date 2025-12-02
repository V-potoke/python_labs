from src.lab04.io_txt_csv import read_text, write_csv
txt = read_text("C:/Users/vende/PycharmProjects/python_labs/data/lab04/input.txt")
write_csv([(2, 1), ("a", "b"), (2,1,3)],
          "C:/Users/vende/PycharmProjects/python_labs/data/lab04/check.csv")
