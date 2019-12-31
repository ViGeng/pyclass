#! /usr/bin/env python3
#  -*- coding: utf-8 -*-

# 大作业 文本统计
# 宋德夫（17307110044）

import re

def how_many_characters(filename):
    
    with open(filename) as file_object:
        contents = file_object.read()

    how_many_characters = len(contents)

    print("{:*^60}\n".format("(how_many_characters)"))
    
    print("\t" + str(how_many_characters))

    
def how_many_lines(filename):
    
    with open(filename) as file_object:
        contents_lines = file_object.readlines()

    how_many_lines = len(contents_lines)

    print("{:*^60}\n".format("(how_many_lines)"))
    
    print("\t" + str(how_many_lines))

def how_many_words(filename):
    
    with open(filename) as file_object:
        contents = file_object.read()
        
    contents = re.sub("-\n", "", contents)

    contents = contents.lower()
    
    words = re.findall(r"\b\w+\b", contents)

    how_many_words = len(words)

    print("{:*^60}\n".format("(how_many_words)"))
    
    print("\t" + str(how_many_words))

def frequency_of_letters(filename):
    
    with open(filename) as file_object:
        contents = file_object.read()
    
    letter_string = re.sub(r"[^a-zA-Z]", "", contents)
    
    letter_string = letter_string.lower()

    letter_dictionary = {}
    
    for letter in letter_string:
        if letter in letter_dictionary.keys():
            letter_dictionary[letter] += 1
        else:
            letter_dictionary[letter] = 1
        
    sorted_list = sorted(letter_dictionary.items(), 
                         key=lambda item:item[1], reverse=True)
    
    how_many_letters = len(letter_string)

    print("{:*^60}\n".format("(frequency_of_letters)"))
    
    for item in sorted_list:
        percentage = item[1] / how_many_letters * 100
        print("\t%-15s%.2f%%" % (item[0], percentage))
        

def high_frequency_words(filename):
    
    with open(filename) as file_object:
        contents = file_object.read()
        
    contents = re.sub("-\n", "", contents)

    contents = contents.lower()
    
    words = re.findall(r"\b\w+\b", contents)
    
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary.keys():
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
    
    sorted_list = sorted(word_dictionary.items(), 
                         key=lambda item:item[1], reverse=True)
    
    first_ten_words = sorted_list[:10]
    
    print("{:*^60}\n".format("(high_frequency_words)"))
    
    for item in first_ten_words:
        print("\t%-15s%d" % (item[0], item[1]))

def high_frequency_words_without_articles(filename):
    
    with open(filename) as file_object:
        contents = file_object.read()
        
    contents = re.sub("-\n", "", contents)

    contents = contents.lower()
    
    words = re.findall(r"\b\w+\b", contents)
    
    word_dictionary = {}
    
    for word in words:
        if word in word_dictionary.keys():
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1
            
    articles = ["a", "an", "the"]

    for article in articles:
        del word_dictionary[article]
        
    sorted_list = sorted(word_dictionary.items(), 
                         key=lambda item:item[1], reverse=True)
    
    first_ten_words_without_articles = sorted_list[:10]
    
    print("{:*^60}\n".format("(high_frequency_words_without_articles)"))

    for item in first_ten_words_without_articles:
        print("\t%-15s%d" % (item[0], item[1]))

def main():

    filename = "bill.txt"
    
    print()

    how_many_characters(filename)

    print()
    
    how_many_lines(filename)

    print()
    
    how_many_words(filename)

    print()
    
    frequency_of_letters(filename)

    print()
    
    high_frequency_words(filename)

    print()
    
    high_frequency_words_without_articles(filename)

    print()

if __name__ == "__main__":
    main()
