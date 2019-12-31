import string
import re

def Sum(text):
    char_sum = 0
    for character in text:
        char_sum += 1
    line_list = re.split("\n",text)
    line_sum = len(line_list)-1
    word_list = re.split(r"\W+",text)
    word_sum = len(word_list)-1
    print("\n字符数:%d, 行数:%d, 单词数:%d"%(char_sum, line_sum, word_sum))

def Frequency(text):
    charSet = string.ascii_lowercase
    letter_dict = dict()
    letter_sum = 0
    for letter in text.lower():
        if letter in charSet:
            letter_dict[letter] = letter_dict.get(letter,0)+1
            letter_sum += 1
    print("\n文件中各字母（不区分大小写）出现的频率（所占百分比）如下：")
    print("\n\t%5s\t%8s"%("字母","百分比"))
    for i in charSet:
        print("\t%5s\t%10.2f%%"%(i,letter_dict.get(i,0)/letter_sum*100))

def Max_Frequency(text,banned_words=[]):
    text = text.lower()
    word_dict = dict()
    word_list = re.split("\W+",text)
    for word in word_list:
        word_dict[word] = word_dict.get(word,0)+1
    word_list = sorted(word_dict.items() , key = lambda t: -t[1])
    print("\n文件中出现频率最高的10个单词及它们出现的次数如下：\n")
    print("\t%3s\t%8s"%("单词","次数"))

    k = 0
    i = 0
    while k <= 10:
        if word_list[i][0] not in banned_words:
            print("\t%5s\t%10d"%(word_list[i][0], word_list[i][1]))
            k += 1
        i += 1

def main():
    file = input("请输入需统计的文件名（包括扩展名）：")
    banned_word_text = input("请输入需排除的单词所在的文件名（包括扩展名）（可不填）：")
    with open(r"%s"%file, encoding='ASCII') as f:
        text = f.read()
    try: 
        with open(r"%s"%banned_word_text, encoding='ASCII') as f:
            banned_words_text = f.read()
        banned_words_list = re.findall(r"\w+", banned_words_text)
    except FileNotFoundError:
        banned_words_list = []

    Sum(text)
    Frequency(text)
    Max_Frequency(text, banned_words_list)

if __name__ == "__main__":
    main() 
