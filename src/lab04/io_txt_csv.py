from pathlib import Path


def ensure_parent_dir(path: Path | str) -> None:
    p = Path(path)
    parent_dir = p.parent

    '''
    Создаёт родительские директории для указанного пути, если их ещё нет.

    Аргументы:
        path: путь к файлу (строка или pathlib.Path).
    '''

    parent_dir.mkdir(parents=True, exist_ok=True)


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    p = Path(path)  # Создаем путь к файлу - Path-объект

    '''
    Открывает текстовый файл и возвращает его содержимое как одну строку.

    Аргументы:
        path: путь к файлу (строка или pathlib.Path).
        encoding: кодировка файла (по умолчанию "utf-8").
                  Если нужна другая, можно указать, например: encoding="cp1251".

    Возвращает:
        str: содержимое файла.

    Падает с ошибками:
        FileNotFoundError: если файл не найден.
    '''

    if not p.exists():
        raise FileNotFoundError('Файл не найден')

    return p.read_text(encoding=encoding)


import csv
from typing import Iterable, Sequence


def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    p = Path(path)  # Создаем путь
    rows = list(rows)

    '''
    Создать или перезаписать CSV-файл с разделителем ','.

    Аргументы:
        rows: последовательность строк (каждая строка — tuple или list).
        path: путь к CSV-файлу (строка или pathlib.Path).
        header: необязательный заголовок (tuple[str,...]), будет записан первой строкой.

    Падает с ошибками:
        ValueError: если не все из строк в rows имеют одинаковую длину.
    '''

    with p.open('w', newline='', encoding='utf-8') as f:
        w = csv.writer(f)  # Создание объекта writer для записи в csv формат
        if header is not None:
            w.writerow(header)  # Записываем заголовок, если такой существует

        if rows:  # Проверка не равную длину строк
            for r in rows:
                if len(r) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")

        for r in rows:
            w.writerow(r)  # Записывает ряды построчно
