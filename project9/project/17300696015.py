f = open ('fudan_history.txt', 'r+' , encoding = 'gbk')
count = 0
line = f.readlines
for index,line in enumerate(f):
    if line == '\n':
        print('')
    else:
        count += 1
        print (index,line)
        


     
