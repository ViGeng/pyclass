#!/usr/bin/env python3
#  -*- coding: utf-8 -*-


import string


def line_counter(file):
    file.seek(0)
    list_f = file.readlines()
    count = len(list_f)
    return count


def character_counter(file):
    file.seek(0)
    string_f = file.read()
    count = len(string_f)
    return count


def word_counter(file):
    file.seek(0)
    string_f = file.read()
    flag = False
    word_dict = dict()
    start = 0
    for i in range(len(string_f)):
        if flag:
            if string_f[i] not in string.ascii_letters:
                if (string_f[i] == '-' and string_f[i+1] == '\n'
                    and string_f[i+2] in string.ascii_letters):
                    flag = True
                elif (string_f[i] == '\n' and string_f[i-1] == '-'
                      and string_f[i+1] in string.ascii_letters):
                    flag = True
                else:
                    flag = False
                    end = i
                    word = string_f[start:end]
                    if word in word_dict:
                        word_dict[word] += 1
                    else:
                        word_dict[word] = 1
        else:
            if string_f[i] in string.ascii_letters:
                flag = True
                start = i
    return word_dict


def letter_counter(file):
    file.seek(0)
    string_f = file.read()
    dict_f = dict()
    for letter in string.ascii_letters:
        dict_f[letter] = 0
    for cha in string_f:
        for letter in string.ascii_letters:
            if cha == letter:
                dict_f[letter] += 1
    return dict_f

        
def main():
    with open('bill.txt','r') as file:            
        line_count = line_counter(file)
        character_count = character_counter(file)
        word_dict = word_counter(file)
        letter_dict = letter_counter(file)
        word_count = 0
        for word in word_dict:
            word_count += word_dict[word]

        print('共计字符数: %d  行数: %d  单词数: %d' %
              (line_count,character_count,word_count))
        print()
        print('=' * 50)
        print()
        
        letter_sum = 0
        for letter in string.ascii_letters:
            letter_sum += letter_dict[letter]
        for letter in string.ascii_lowercase:
            frequence = (letter_dict[letter]
                         +letter_dict[letter.upper()])/ letter_sum
            print("'%s' 和 '%s' 出现的频率是: %-.4f%s" %
                  (letter,letter.upper(),frequence*100,'%'))
        print()
        print('=' * 50)
        print()

        print('出现频率最高的10个单词是：')
        print()
        list_exception = ['the','and','to','of','a','that']
        list_exception_upper = [(word[0].upper() + word[1:])
                                 for word  in list_exception]
        list_word = sorted(word_dict.items(),key =
                           lambda item:item[1],reverse = True)
        i = 0
        for word in list_word:
            if (word[0] not in list_exception) and (
                word[0] not in list_exception_upper):
                i += 1
                print("%-2d  %-6s 出现了 %-d 次" % (i,"'" + word[0] + "'"
                                         ,word_dict[word[0]]))
            if i >= 10:
                break


if __name__ == '__main__':
    main()
