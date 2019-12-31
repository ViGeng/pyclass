file = 'bill.txt'
f = open(file, 'r')
lines = f.readlines()
f.close()
character_count = 0
line_count = 0
letter_dic = {}
letter_count = 0
word_dic = {}
line_count = len(lines)

# 排除词列表
stop_words = ['the', 'and', 'i', 'to', 'of', 'a', 'my', 'in', 'you',
              'that', 'is', 'for', 'with', 'not', 'your', 'his', 'be',
              'this', 'as', 'but', 'he', 'it', 'have', 'thou', 'me',
              'will', 'by', 'so', 'thy', 'what', 'are', 'if', 'shall',
              'do', 'all', 'we', 'him', 'or', 'our', 'her', 'no', 'on',
              'from', 'at', 'they', 'would', 'which', 'was', 'let', 'their',
              'she', 'am', 'how', 'when', 'than', 'an', 'hath', "i'll",
              'may', 'upon', 'such', 'more', 'were', 'did', 'one', 'o', 'then']

# 下一行是否忽略第一个单词，考虑行尾单词折行
is_ignore_first_word = False
for i in range(line_count):
    line = lines[i]
    character_count += len(line)

    # 去除换行符
    line = line[:-1]
    for item in line:
        item = item.lower()
        if 'a' <= item <= 'z':
            letter_count += 1
            if item in letter_dic:
                letter_dic[item] += 1
            else:
                letter_dic[item] = 1
    words = line.split(' ')
    if is_ignore_first_word:
        words = words[1:]
    for word in words:
        word = word.lower()
        # 如果是空的，直接跳过
        if word == '':
            continue
        # 去掉句尾的.或者,
        if word[-1] == '.' or word[-1] == ',':
            word = word[:-1]
        # 去除在排除词列表中的单词
        if word == '' or word in stop_words:
            continue
        # 判断是否为行尾单词折行
        if word[-1] == '-':
            is_ignore_first_word = True
            word = word + lines[i+1].split(' ')[0]
        else:
            is_ignore_first_word = False
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1

print('文件的字符（包括空格、换行等所有字符）总数为：', character_count)
print('文件的总行数为：', line_count)

sorted_letters = sorted(letter_dic.items(), key=lambda item: item[0])
print('文件中各字母（不区分大小写）占字母总数的百分比为：')
for item in sorted_letters:
    print('{0}:    {1:.3%}'.format(item[0], item[1] / letter_count))

sorted_words = sorted(word_dic.items(), key=lambda item: item[1], reverse=True)

print('文件中前10个高频单词（不区分大小写）为：')
for item in sorted_words[:10]:
    print(('{0}:' + (12 - len(item[0])) * ' ' + '{1}').format(item[0], item[1]))
