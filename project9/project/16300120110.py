import project9_util as util

encodings = util.detect_encoding('fudan_history.txt')
a = encodings
name = util.nl_filename('fudan_history.txt')


def main():
    with open('fudan_history.txt','r',encoding = a) as file:
        next (file)
        i = 0
        for line in file.readlines():
            if len(line.strip()) == 0:
                print (line)
            else:
                i += 1
                print('%-5d%s' % (i,line))

if __name__ == '__main__':
    main()



