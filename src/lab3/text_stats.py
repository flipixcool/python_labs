from text import tokenize, top_n, count_freq
import sys


def main():
    text = sys.stdin.read()
    words = tokenize(text.lower())
    freq = count_freq(words)

    max_width = max(len(word) for word, _ in top_n(freq, 5))
    print(f"{'слово'.ljust(max_width)} | частота")
    print('-' * (max_width + 10))
    for word, count in top_n(freq, 5):
        print(f"{word.ljust(max_width)} | {count}")

if __name__ == "__main__":
    main()
