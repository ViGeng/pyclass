file = open('fudan_history.txt',encoding='gbk')
text = file.readlines()

with open('fudan_history_nl.txt', 'w', encoding='gbk') as b_file:
    i = 1
    for line in text:
        line = line.strip(' ')
        if not line:
            break
        elif line == '\n':
            b_file.writelines('\n')
        else:
            f = '{:<3}{}'.format(i, line)
            b_file.writelines(f)
            i += 1
            
