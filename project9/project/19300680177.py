def main():
    file = open('fudan_history.txt',encoding='gbk')
    text = file.readlines()
    with open('fudan_history_nl.txt','w',encoding='gbk')as file2:
        i = 1
        for line in text:
            line = line.strip(' ')
            if not line:
                break
            elif line == '\n':
                file2.writelines('\n')
            else:
                f = '{:<3}{}'.format(i, line)
                file2.writelines(f)
                i += 1
if __name__ == '__main__':
    main()
