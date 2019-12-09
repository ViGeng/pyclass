

import project9_util as pro

with open('fudan_history.txt','r') as file:
    lines = file.readlines()#列表，读取所有行
    
#print (lines)

row_count = 1
newlines = []

for line in lines:
    if line.strip() == '':
        newline = '\n'
    else:
        newline = '    '+str(row_count)+'  '+line
        row_count += 1
    
    newlines.append(newline)
   
#文件名字
name = pro.nl_filename('fudan_history.txt')
with open(name,'w') as file:
    file.writelines(newlines)

f = open(name,'r')
print(f.read())

#编码是否一致？
encode1 = pro.detect_encoding('fudan_history.txt')
encode2 = pro.detect_encoding(name)

if encode1 == encode2:
    print('yes')
else:
    print('no')
