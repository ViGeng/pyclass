import project9_util
text = 'fudan_history.txt'
fudan_history_n1 = project9_util.nl_filename('fudan_history.txt')
encoding = project9_util.detect_encoding('fudan_history.txt')


def  add_number(file1 = 'fudan_history.txt'):
    fp = open(file1)
    f1 = fp.readlines()
    count = 0
    with open('fudan_history_n1.txt' , mode = 'w',encoding = encoding) as file:
        for i in f1:
            if len(i.strip()) == 0:
                file.write('\n')
            else:
                count += 1
                file.write(('%d %s')%(count, i))

    return


if __name__ == '__main__':
    add_number(file1 = 'fudan_history.txt')





            
