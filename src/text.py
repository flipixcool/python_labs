def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')

    for i in ['\t', '\r', '\n', '\f', '\v']:
        text = text.replace(i, ' ')

    while '  ' in text:
        text = text.replace('  ', ' ')

    return text.strip()

# print(normalize("ПрИвЕт\nМИр\t"))
# print(normalize("ёжик, Ёлка"))
# print(normalize("Hello\r\nWorld"))
# print(normalize("  двойные   пробелы  "))


def tokenize(text: str) -> list[str]:
    lst = []
    current_word = []
    i = 0
    while i < len(text):
        c = text[i]
        if c.isalnum() or c == '_':
            current_word.append(c)
        elif c == '-':
            if current_word and i + 1 < len(text) and (text[i + 1].isalnum() or text[i + 1] == '_'):
                current_word.append(c)
            else:
                if current_word:
                    lst.append(''.join(current_word))
                    current_word = []
        else:
            if current_word:
                lst.append(''.join(current_word))
                current_word = []
        i += 1
    if current_word:
        lst.append(''.join(current_word))
    return lst

# print(tokenize("привет мир"))
# print(tokenize("hello,world!!!"))
# print(tokenize("по-настоящему круто"))
# print(tokenize("2025 год"))
# print(tokenize("emoji 😀 не слово"))

def count_freq(tokens: list[str]) -> dict[str, int]:
    d = {}
    for word in tokens:
        if word not in d:
            d[word] = 1
        else:
            d[word] += 1
    return dict(sorted(d.items()))

# print(count_freq(["a","b","a","c","b","a"]))
# print(count_freq(["bb","aa","bb","aa","cc"]))

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    # Сортируем пары (слово, частота) по убыванию частоты
    sorted_counts = sorted(freq.items(), key=lambda item: item[1], reverse=True)
    return sorted_counts[:n]

# print(top_n(count_freq(["a","b","a","c","b","a"]), n=2))
# print(top_n(count_freq(["bb","aa","bb","aa","cc"]), n=2))


# normalize
assert normalize("ПрИвЕт\nМИр\t") == "привет мир"
assert normalize("ёжик, Ёлка") == "ежик, елка"

# tokenize
assert tokenize("привет, мир!") == ["привет", "мир"]
assert tokenize("по-настоящему круто") == ["по-настоящему", "круто"]
assert tokenize("2025 год") == ["2025", "год"]

# count_freq + top_n
freq = count_freq(["a","b","a","c","b","a"])
assert freq == {"a":3, "b":2, "c":1}
assert top_n(freq, 2) == [("a",3), ("b",2)]

# тай-брейк по слову при равной частоте
freq2 = count_freq(["bb","aa","bb","aa","cc"])
assert top_n(freq2, 2) == [("aa",2), ("bb",2)]