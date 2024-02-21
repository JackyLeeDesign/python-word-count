import jieba
import sys

def count_words(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            contents = file.read()
    except FileNotFoundError:
        print(f"Sorry, the file {filename} does not exist.")
        return

    words = jieba.cut(contents, cut_all=False)
    word_count = {}

    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1

    for word, count in word_count.items():
        print(f"'{word}' occurs {count} times in the file.")

if __name__ == "__main__":
    count_words(sys.argv[1])