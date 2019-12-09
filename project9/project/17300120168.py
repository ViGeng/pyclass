import project9_util as util
import string


def add_text():
    with open('project9_util.py', 'a') as f:
        util.detect_encoding('project9_util.py')
        with open ('fudan_history.txt') as file:
            text = file.read()
            object = text.splitlines()
            n = 1
            add_text = []
            for item in object:
                if item != ' ' and item !='':
                    item = str(n) + ' ' + item
                    n += 1
                    add_text.append(item)
                else:
                    add_text.append(item)
            util.nl_filename('fudan_history')
            with open('fudan_history_nl.txt','w',encoding='utf-8') as target:
                for item in add_text:
                    item = item + '\n'
                    target.write(item)
                    target.flush()
           
        
if __name__ == '__main__':
     add_text()
