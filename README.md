# Python-Word-Counter

## Introduction :

The Python Word Counter is a Python script that takes a filename as input and prints out the count of each word in the file. This version has been updated to handle Chinese word segmentation.

## input

```bash
在這個數位時代，學習編程語言變得越來越重要。Python 是一種非常受歡迎的編程語言，它的語法簡單易懂，適合初學者學習。

In the digital age, learning to code has become increasingly important. Python is a very popular programming language. Its syntax is simple and easy to understand, making it suitable for beginners.

無論你是想做網頁開發、數據分析還是機器學習，Python 都是一個很好的選擇。希望你在學習 Python 的旅程中能夠獲得滿足感和成就感。

Whether you want to do web development, data analysis, or machine learning, Python is a great choice. I hope you find satisfaction and a sense of accomplishment in your journey to learn Python.
```

## Output

```bash
'在' occurs 2 times in the file.
'這個' occurs 1 times in the file.
'數位' occurs 1 times in the file.
'時代' occurs 1 times in the file.
'，' occurs 4 times in the file.
'學習' occurs 4 times in the file.
'編程' occurs 2 times in the file.
'語言變' occurs 1 times in the file.
'得' occurs 1 times in the file.
'越來' occurs 1 times in the file.
'越' occurs 1 times in the file.
'重要' occurs 1 times in the file.
'。' occurs 4 times in the file.
'Python' occurs 6 times in the file.
' ' occurs 66 times in the file.
'是' occurs 3 times in the file.
'一種' occurs 1 times in the file.
'非常' occurs 1 times in the file.
'受歡' occurs 1 times in the file.
'迎' occurs 1 times in the file.
'的' occurs 4 times in the file.
'語言' occurs 1 times in the file.
'它' occurs 1 times in the file.
'語法' occurs 1 times in the file.
'簡單' occurs 1 times in the file.
'易懂' occurs 1 times in the file.
'適合' occurs 1 times in the file.
'初學者' occurs 1 times in the file.
'
' occurs 6 times in the file.
'In' occurs 1 times in the file.
'the' occurs 1 times in the file.
'digital' occurs 1 times in the file.
'age' occurs 1 times in the file.
',' occurs 5 times in the file.
'learning' occurs 2 times in the file.
'to' occurs 4 times in the file.
'code' occurs 1 times in the file.
'has' occurs 1 times in the file.
'become' occurs 1 times in the file.
'increasingly' occurs 1 times in the file.
'important' occurs 1 times in the file.
'.' occurs 5 times in the file.
'is' occurs 3 times in the file.
'a' occurs 3 times in the file.
'very' occurs 1 times in the file.
'popular' occurs 1 times in the file.
'programming' occurs 1 times in the file.
'language' occurs 1 times in the file.
'Its' occurs 1 times in the file.
'syntax' occurs 1 times in the file.
'simple' occurs 1 times in the file.
'and' occurs 2 times in the file.
'easy' occurs 1 times in the file.
'understand' occurs 1 times in the file.
'making' occurs 1 times in the file.
'it' occurs 1 times in the file.
'suitable' occurs 1 times in the file.
'for' occurs 1 times in the file.
'beginners' occurs 1 times in the file.
'無論' occurs 1 times in the file.
'你' occurs 2 times in the file.
'想' occurs 1 times in the file.
'做' occurs 1 times in the file.
'網頁' occurs 1 times in the file.
'開發' occurs 1 times in the file.
'、' occurs 1 times in the file.
'數據' occurs 1 times in the file.
'分析' occurs 1 times in the file.
'還是' occurs 1 times in the file.
'機器' occurs 1 times in the file.
'都' occurs 1 times in the file.
'一個' occurs 1 times in the file.
'很' occurs 1 times in the file.
'好' occurs 1 times in the file.
'選擇' occurs 1 times in the file.
'希望' occurs 1 times in the file.
'旅程' occurs 1 times in the file.
'中能夠' occurs 1 times in the file.
'獲得' occurs 1 times in the file.
'滿足感' occurs 1 times in the file.
'和' occurs 1 times in the file.
'成就感' occurs 1 times in the file.
'Whether' occurs 1 times in the file.
'you' occurs 2 times in the file.
'want' occurs 1 times in the file.
'do' occurs 1 times in the file.
'web' occurs 1 times in the file.
'development' occurs 1 times in the file.
'data' occurs 1 times in the file.
'analysis' occurs 1 times in the file.
'or' occurs 1 times in the file.
'machine' occurs 1 times in the file.
'great' occurs 1 times in the file.
'choice' occurs 1 times in the file.
'I' occurs 1 times in the file.
'hope' occurs 1 times in the file.
'find' occurs 1 times in the file.
'satisfaction' occurs 1 times in the file.
'sense' occurs 1 times in the file.
'of' occurs 1 times in the file.
'accomplishment' occurs 1 times in the file.
'in' occurs 1 times in the file.
'your' occurs 1 times in the file.
'journey' occurs 1 times in the file.
'learn' occurs 1 times in the file.
```

## Code

```python
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
```

## Usage

To use this script, run the following command:

```bash
python count_words.py yourfile.txt
```

Please note that this script requires the jieba library for Chinese word segmentation. If you haven't installed it yet, you can do so with the following command:

```bash
pip install jieba
```