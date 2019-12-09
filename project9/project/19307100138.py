file=open("D:/python/9/fudan_history.txt.txt","r")
lines=file.readlines()
for index,item in enumerate(lines):
    if item.isspace():
        item="\n"
        print(item)
    else:
        print(index,item)
        pass
file.close()


