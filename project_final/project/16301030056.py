from string import ascii_lowercase

keep = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
        'w', 'x', 'y', 'z', ' ', '-', "'"]
stop_words = ['the', 'and', 'i', 'to', 'of', 'a', 'you', 'my', 'that', 'in', 'she', 'he', 'her', 'his', 'it', 'be',
              'was', 'had']


def get_letter_count(str_c):
    str_letter = ascii_lowercase
    dict_letter = {}
    for letter in str_letter:
        dict_letter[letter] = []
    for i in str_c:
        if i.lower() not in ascii_lowercase:
            continue
        dict_letter[i.lower()].append(i)
    total = sum([len(dict_letter[count]) for count in str_letter if len(dict_letter[count]) != 0])
    for count in str_letter:
        if len(dict_letter[count]) != 0:
            rate = "%.2f%%" % (len(dict_letter[count]) / total * 100)
            print("%s出现的频率为%s" % (count, rate))


def normalize(s):
    result = ''
    for c in s.lower():
        if c in keep:
            result += c
    return result


def make_dict(s):
    words = normalize(s).split()
    d = {}
    for w in words:
        if w in d:
            d[w] += 1
        else:
            d[w] = 1
    return d


def file_status(f):
    c = open(f).read()
    print('字符数：', len(c))
    print('行数：', c.count('\n'))
    print('单词数：', len(normalize(c).split()))
    get_letter_count(c)
    d = make_dict(c)
    lst = [(d[w], w) for w in d]
    lst.sort()
    lst.reverse()
    print('出现频率最高的10个单词及它们出现的次数：')
    i = 1
    for count, word in lst[:10]:
        print('%d. %4d %s' % (i, count, word))
        i += 1
    print('出现频率最高的10个单词及它们出现的次数(忽略排除词后)：')
    j = 1
    for count, word in lst[:]:
        if word not in stop_words:
            print('%d. %4d %s' % (j, count, word))
            j += 1
        if j == 11:
            break


file_status('bill.txt')
