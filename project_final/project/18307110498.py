file=open("bill.txt","r")
lines=file.readlines()
list1="".join(lines)
print("有%d个字符"%len(list1))
print("有%d行"%len(lines))
list2=list1.split()
list3=" ".join(list2)


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

print("有%d个单词"%len(list0))

list4=list0.replace(" ","")
list5=list4.lower()
d={}
for i in (list(set(list5))):
    d[i]="%f%%"%((list5.count(i))*100/len(list5))
item=(sorted(d.items(),key=lambda x:x[0],reverse=False))
print("各字母（不区分大小写）出现的频率:")
print(item)

list6=list0.lower()


ss = list6.replace('and','')
ss = ss.replace('but','')
ss = ss.replace('then','')
ss = ss.replace('the','')
ss = ss.replace('a','')
ss = ss.replace('or','')
ss = ss.replace('so','')

list7=ss.split()
print("出现频率最高的10个单词及它们出现的次数:")
import sys,re
d={}
num=[]

for k in list7:
    if not d.get(k):
        d[k]=1
    else:
        d[k]+=1
for v in d.values():
    if v not in num:
        num.append(v)
num.sort()
num=num[-10:]

d=sorted(d.items(),key=lambda d:d[1],reverse=True)
for i in d:
    if i[1] in num:
        print(i)


