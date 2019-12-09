file = open("fudan_history.txt","r")
lines = file.readlines()
x=0
for line in lines:
    line = line.strip()
    if not len(line):
        print()
        continue
    else:
        x+=1
        print('%s %s'%(x, line))
        print()
file.close()
