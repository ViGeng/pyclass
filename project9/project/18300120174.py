import project9_util as util

with open("fudan_history.txt", encoding = util.detect_encoding("fudan_history.txt")) as file:
    s = file.read()
    
s = s.strip()
list1 = s.split('\n')
i = 1
list2 = []

for line in list1:
    if line:
        list2.append(str(i)+' '+line+'\n')
        i = i+1
    else:
        list2.append(line+'\n')

file.close()

with open(util.nl_filename("fudan_history.txt"), "w") as nlf:
    nlf.writelines(list2) 
