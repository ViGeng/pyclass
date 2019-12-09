i = 0    
with open('fudan_history.txt','r') as f1,open('fudan_history_nl.txt','w') as f2:
    for line in f1:
        if line !='' and line !='\n':
            i=i+1
            index = line.find('')
            f2.write(str(i) + " " +line[index:])
        else:
             i=i
             index = line.find('')
             f2.write(line[index:])
  
