answer = [(gong, mu, chu)\
         for gong in range (100+1)\
         for mu in range (100+1)\
         for chu in range (100+1)\
           if gong + mu + chu==100 and gong*5 + mu*3 + chu*1/3==100]
print ('总共有%d个解'%len(answer))
for i in range(len(answer)):
   cock, hen, chick = answer[i]
   print('解%d:鸡翁有%d只，鸡母有%d只， 鸡雏有%d只'%((i+1),cock,hen,chick))
