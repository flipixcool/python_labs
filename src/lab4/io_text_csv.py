from pathlib import Path
import csv


def read_text(path: str | Path, encoding: str = "utf-8") -> str:
    """encoding (str, по умолчанию "utf-8"): Кодировка файла.
            Если требуется открыть файл в другой кодировке, укажите ее явно,
            например: encoding='cp1251'"""
    with open(path, encoding=encoding) as file:
        return file.read()

# txt = read_text("data/input.txt")
# print(txt)

def write_csv(rows: list[tuple | list], path: str | Path, header: tuple[str, ...] | None = None) -> None:
    if not rows:
        return 
    
    length = len(rows[0])
    for row in rows:
        if len(row) != length:
            raise ValueError

    with open(path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        if header:
            writer.writerow(header)
        writer.writerows(rows)

write_csv([("word","count"),("test",3)], "data/check.csv")