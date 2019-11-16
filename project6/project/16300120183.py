# -*- coding: utf-8 -*-
   
def method_1():#循环结构
    items_1=[]
    for cock in range(0,20):
        for hen in range(0,int((100-5*cock)/3)):
            chick=(100-(5*cock+3*hen))*3
            if cock+hen+chick==100:
                items_1.append((cock,hen,chick))
    print('总共有%d个解' %len(items_1))
    x=1
    for it in items_1:
        print('解%d：鸡翁 %s 鸡母 %s 鸡雏 %s'%(x,it[0],it[1],it[2]))
        x=x+1
        

def method_2():#；列表解析式
   cock_p,hen_p,chick_p=5,3,1.0/3
   cock_n,hen_n,chick_n=range(0,int(100/cock_p)),range(0,int(100/hen_p)),range(0,int(100/chick_p))
   items=[(cock,hen,chick) for cock in cock_n for hen in hen_n for chick in chick_n
          if int(cock*cock_p+hen*hen_p+chick*chick_p)==100 and chick%3==0 and cock+hen+chick==100]
   print('总共有%d个解' %len(items))
   x=1
   for it in items:
       print('解%d：鸡翁 %s 鸡母 %s 鸡雏 %s'%(x,it[0],it[1],it[2]))
       x=x+1

if __name__ == '__main__':
    method_1()
    method_2()