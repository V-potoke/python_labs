import re


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