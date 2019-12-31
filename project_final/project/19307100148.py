import sys,re,collections
import numpy as np

# patterns that used to find or/and replace particular chars or words
# to find chars that are not a letter, a blank or a quotation
pat_letter = re.compile(r'[^a-zA-Z | \- \']+')
pat_sub = re.compile(r'[*\-\-]{2,}')
# to find the 's following the pronouns. re.I is refers to ignore case
pat_is = re.compile("(it|he|she|that|this|there|here)(\'s)", re.I)
# to find the 's following the letters
pat_s = re.compile("(?<=[a-zA-Z])\'s")
# to find the ' following the words ending by s
pat_s2 = re.compile("(?<=s)\'s?")
# to find the abbreviation of not
pat_not = re.compile("(?<=[a-zA-Z])n\'t")
# to find the abbreviation of would
pat_would = re.compile("(?<=[a-zA-Z])\'d")
# to find the abbreviation of will
pat_will = re.compile("(?<=[a-zA-Z])\'ll")
# to find the abbreviation of am
pat_am = re.compile("(?<=[I|i])\'m")
# to find the abbreviation of are
pat_are = re.compile("(?<=[a-zA-Z])\'re")
# to find the abbreviation of have
pat_ve = re.compile("(?<=[a-zA-Z])\'ve")

# Statistics file lines
def count_lines(filepath):
    try:
        text = open(filepath,'r').readlines()
    except:
        print ("\nfile.txt is not exist!")
    return len(text)
    
def get_words(filepath):
    try:
        text = open(filepath,'r')
    except:
        print ("\nfile.txt is not exist!")
    words_box=[]
    for line in text:
        '''
        TO DO
        I'm not sure whether words like 'I'm' or 'it's' count as one word or two words.
        If you think of 'I'm' as one word, please use function: replace_abbreviations1()
        If you think of 'I'm' as 'I am', please use function: replace_abbreviations2()
        '''
        new_text = replace_abbreviations1(line).split()
        words_box.extend(new_text)
    return(words_box)

def count_words(filepath):
    words_list = get_words(filepath)
    print('Total number of words: %s' % len(words_list))
    '''
    TO DO 
    You can add words to ignore in the ignore_list
    '''
    ignore_words = ["of","the","for"]
    print("Top 10:")
    temp = collections.Counter(words_list)
    for i in ignore_words:
        if i not in words_list:
            ignore_words.remove(i)
    for i in ignore_words:
        del temp[i]
    temp = temp.most_common(10)
    for t in temp:
        print(t[0],":\t",t[1])

def statistics_letters(filepath):
    words_list = get_words(filepath)
    s = "".join(words_list)
    count_a_z = np.zeros(26)
    for i in s:
        delta = ord(i) - 97
        if delta >=0 and delta <= 26:
            count_a_z[delta] += 1
    summ = np.sum(count_a_z)
    dict_letters = {}
    for i in range(26):
        dict_letters[str(chr(i+97))]=round(count_a_z[i]/summ,2)
    j = 0
    for i in range(26):
        j+=1
        print('%.2f%%' % (dict_letters[chr(i+97)] * 100),"\t",end="")
        if j == 10:
            print("")
            j = 0
    print("")

def replace_abbreviations1(text):
    new_text = text
    new_text = pat_letter.sub(' ', text).strip().lower()
    new_text = pat_sub.sub(' ', new_text)

    return new_text

def replace_abbreviations2(text):
    new_text = text
    new_text = pat_letter.sub(' ', text).strip().lower()
    new_text = pat_sub.sub(' ', new_text)
    new_text = pat_is.sub(r"\1 is", new_text)
    new_text = pat_s.sub("", new_text)
    new_text = pat_s2.sub("", new_text)
    new_text = pat_not.sub(" not", new_text)
    new_text = pat_would.sub(" would", new_text)
    new_text = pat_will.sub(" will", new_text)
    new_text = pat_am.sub(" am", new_text)
    new_text = pat_are.sub(" are", new_text)
    new_text = pat_ve.sub(" have", new_text)
    new_text = new_text.replace('\'', ' ')

    return new_text

def count_characters(filepath):
    try:
        text = open(filepath,'r').read()
    except:
        print ("\nfile.txt is not exist!")
    lines = count_lines(filepath)
    return (len(text)-lines)

if __name__ == "__main__":
    '''
    Question 1: How many charactors,lines or words.
    Question 2: The percentage of each letter.
    Question 3: Top ten most appeared words.
    '''
    print('Total number of charactors: %s' % count_characters('./bill.txt'))
    print('Total number of lines: %s' % count_lines('./bill.txt'))
    #includ Q1 and Q3
    count_words('./bill.txt')
    statistics_letters('./bill.txt')