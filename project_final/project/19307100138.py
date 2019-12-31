file=open("bill.txt","r")
lines=file.readlines()
list1=" ".join(lines)#原始字符串
print("有%d个字符"%len(list1))
print("有%d行"%len(lines))
list2=list1.split()
list3=" ".join(list2)#没有空行的字符串
list0=list3.replace(",","")
list0=list0.replace("[","")
list0=list0.replace("]","")
list0=list0.replace("(","")
list0=list0.replace(")","")
list0=list0.replace("#","")
list0=list0.replace("@","")
list0=list0.replace("$","")
list0=list0.replace("%","")
list0=list0.replace("'","")
list0=list0.replace('"',"")
list0=list0.replace("1","")
list0=list0.replace("2","")
list0=list0.replace("3","")
list0=list0.replace("4","")
list0=list0.replace("5","")
list0=list0.replace("6","")
list0=list0.replace("7","")
list0=list0.replace("8","")
list0=list0.replace(".","")
list0=list0.replace("!","")
list0=list0.replace("/","")
list0=list0.replace("<","")
list0=list0.replace(">","")
list0=list0.replace("&","")
list0=list0.replace("*","")
list0=list0.replace("-","")
list0=list0.replace("_","")
list0=list0.replace("`","")
list0=list0.replace("0","")
list0=list0.replace("9","")
list0=list0.replace(":","")
list0=list0.replace(";","")
list0=list0.replace("?","")
list0=list0.replace("|","")
list0=list0.replace("~","")
list0=list0.replace("}","")
list4=list0.replace(" ","")#去掉了空格
print("有%d个单词"%len(list0))
#这是统计字母的方法
list5=list4.lower()#变成了小写字母
dic={}
for i in (list(set(list5))):
    dic[i]="%f%%"%((list5.count(i))*100/len(list5))
item=(sorted(dic.items(),key=lambda x:x[0],reverse=False))
print("字母出现的频率是:")
print(item)
list6=list0.lower()
import re
result=re.sub(r'\band\b',"",list6)
result=re.sub(r'\bof\b',"",result)
result=re.sub(r'\ba\b',"",result)
result=re.sub(r'\bin\b',"",result)
result=re.sub(r'\bto\b',"",result)
result=re.sub(r'\bthis\b',"",result)
result=re.sub(r'\bthat\b',"",result)
result=re.sub(r'\bthe\b',"",result)
result=re.sub(r'\bor\b',"",result)
result=re.sub(r'\bit\b',"",result)
result=re.sub(r'\bfor\b',"",result)
result=re.sub(r'\bbe\b',"",result)
result=re.sub(r'\bbut\b',"",result)
list7=result.split()
print("出现次数最多的前10个单词及其个数是:")
import sys,re
distone={}
numTen=[]

for keyone in list7:
    if not distone.get(keyone):
        distone[keyone]=1
    else:
        distone[keyone]+=1
for v in distone.values():
    if v not in numTen:
        numTen.append(v)
numTen.sort()
numTen=numTen[-10:]

distone=sorted(distone.items(),key=lambda d:d[1],reverse=True)
for i in distone:
    if i[1] in numTen:
        print(i)




