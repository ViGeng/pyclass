def count_characters(text):
    text = text.splitlines()
    number_characters = 0
    for line in text:
        number_characters = number_characters + len(line)
        pass
    print('该文本文件包含%s个字符' % number_characters)


def count_lines(text):
    number_lines = text.count('\n') + 1
    print('该文本文件包含%s行' % number_lines)
    

def count_words(text):
    object = text.lower()
    repetition = object.count('-')
    for ch in object:
        if ch not in string.ascii_letters:
            object = object.replace(ch, ' ')
        else:
            pass
    words = object.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    raw_number_words = 0
    items.sort(key=lambda x:x[1], reverse=True)
    for item in items:
        raw_number_words += item[1]
    real_number_words = raw_number_words - repetition
    print('该文本包含%d个单词' % (real_number_words))

    
import string
def count_letter_percentage(text):
    alist = list(text)
    number_letters = 0
    for letter in alist:
        if letter in string.ascii_letters:
            number_letters += 1
        else:
            pass
    object = text.lower()
    for ch in object:
        if ch not in string.ascii_letters:
            object = object.replace(ch, ' ')
        else:
            pass
    for letter in ['a', 'b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
        percentage = object.count(letter) / number_letters * 100
        print('文件中%s出现的频率是%.2f%%' % (letter,percentage))
        print()
    pass
        
    


def count_most_words(text):
    object = text.lower()
    for ch in object:
        if ch not in string.ascii_letters:
            object = object.replace(ch, ' ')
        else:
            pass
    words = object.split()
    counts = {}
    for word in words:
        counts[word] = counts.get(word,0)+1
    items = list(counts.items())
    items.sort(key=lambda x:x[1], reverse=True)
    
    most_words_list = items[:10]
    print('文件中出现频率最高的10个单词及它们出现的次数:')
    for item in most_words_list:
        print('%-10s  %-15s' % (item[0], item[1]))
    
    
    
def main():
    with open('bill.txt') as f:
        text = f.read()
    print()
    count_characters(text)
    print()
    count_lines(text)
    print()
    count_words(text)
    print()
    count_letter_percentage(text)
    print()
    count_most_words(text)
   
    

if __name__ == '__main__':
    main()
