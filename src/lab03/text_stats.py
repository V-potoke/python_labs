import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))
from src.lib.text import count_freq, top_n, normalize, tokenize

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
