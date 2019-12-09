import project9_util
text = 'fudan_history.txt'
newname = project9_util.nl_filename('fudan_history.txt')
encoding = project9_util.detect_encoding('fudan_history.txt')


def  add_order_number(file1 = 'fudan_history.txt'):
    fp = open(file1)
    c = fp.readlines()
    b = 0
    with open('newname.txt' , mode = 'w',encoding = encoding) as file:
        for i in c:
            if len(i.strip()) != 0:
                b += 1
                file.write(('%-5d %s')%(b, i))
            else:
                file.write('\n')
    return


if __name__ == '__main__':
    add_order_number(file1 = 'fudan_history.txt')





            
