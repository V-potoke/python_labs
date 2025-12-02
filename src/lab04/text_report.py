from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

txt = read_text('C:/Users/vende/PycharmProjects/python_labs/data/lab04/input.txt', 'cp1251')
txt = tokenize(normalize(txt))
txt_counts = top_n(count_freq(txt))
print('Всего слов:', len(txt))
print('Уникальных слов:', len(set(txt)))
print('Топ-5:')
for i in txt_counts:
    print( f'{i[0]}:{i[1]}')

write_csv(txt_counts,
          'C:/Users/vende/PycharmProjects/python_labs/data/lab04/report.csv',
          ("word","count"))
