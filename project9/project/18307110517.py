import re

def detect_encoding(text):
    """探测文件的编码方式
    参数：文件名， 返回探测到的编码方式
    """

    # UTF-8-SIG
    encodings = 'ASCII', 'UTF-8', 'GBK'

    for encoding in encodings:
        try:
            with open(text, encoding=encoding) as f:
                f.read(100)
            break
        except UnicodeDecodeError:
            pass
    return encoding


def nl_filename(name):
    """ 返回一个新的文件名，传递的参数name为文件名
    """

    if name.endswith(('.txt', '.py')):
        dot_pos = name.rindex('.')
        return name[0:dot_pos] + '_nl' + name[dot_pos:]
    else:
        return name + '_nl'

# if __name__ == '__main__':
#     print('%s-->%s: %s' %
#           (__file__, nl_filename(__file__), detect_encoding(__file__)))

#     text = 'fudan_history.txt'
#     print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))

print('示例：Please input： fudan_history_nl.txt and enter')
text = input()
encoding = detect_encoding(text)
file = open(text,"r",encoding = encoding)
lines = file.readlines()
file.close()
name = nl_filename(text)
f1 = open(name, "a+", encoding = encoding)
i = 1
for line in lines:
    print(line)
    if i == 1:
        f1.write(str(i) + ' ')
        i = i + 1
    elif line != '\n' and line != '':
        f1.write(line + '\n' + str(i) + ' ')
        i = i + 1
f1.close()
