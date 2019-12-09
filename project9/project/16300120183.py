
import codecs
import project9_util as util

def fd():

    fdhis = "fudan_history.txt"
    enc = util.detect_encoding(fdhis)
    with codecs.open(fdhis,encoding=enc) as file:
        lines = file.readlines()

    newfile = util.nl_filename(fdhis)

    row_count = 1
    with codecs.open(newfile,"w",encoding=enc) as newfile2:
        for line in lines:
            if not line.split():
                newfile2.write(' '*5+line)
                continue
            newfile2.write("%-5d"%row_count+line)
            row_count += 1

if __name__ == '__main__':
    fd()

        
