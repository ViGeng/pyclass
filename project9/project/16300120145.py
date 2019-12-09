import project9_util as util

def line_number():
    with open('fudan_history.txt','r') as filename:
        lines = filename.readlines()
    with open('fudan_history_nl.txt','w') as filename:
        pline = 0
        for line in lines:
            n_line = line.strip()
            if len(n_line):
                pline = pline + 1
                print(str(pline)+ n_line + '\n')
                filename.write(str(pline) + n_line + '\n')
            else:
                del line
                print('\n')
                filename.write('\n')

if __name__ == '__main__':
    line_number()




    
    
    
