

def main():
    bill=open("bill.txt")
    lnum=0
    cnum=0
    wnum=0
    wdict={}
    cdict={}
    for line in bill:
        lnum+=1  #行数
        for char in line:
            cnum+=1  #字符
            char=char.lower()
            if char.isalpha() and char in cdict:
                cdict[char]+=1
            elif char.isalpha():
                cdict[char]=1
        words = line.split()
        wlen=len(words)
        #print(wlen)
        wn=0
        lastflag=0
        for word in words:
            wn+=1 
            if wn==wlen-1:
                wwlen=len(word)
                if word[wwlen-1]=='-':
                    wn-=1
                    lastw=word[0:wwlen-1]
                    lastflag=1
                    continue
                else:
                    lastflag=0
            if wn==1 and lastflag==1:
                word=lastw+word  
            word=word.lower()
            if word in wdict:
                wdict[word]+=1
            else:
                wdict[word]=1
        wnum=wnum+wn  #单词
    print("在文本文件中，包含%d个字符，%d行，%d个单词" %(cnum,lnum,wnum))        
    #字母出现的频率
    print("文件中各字母出现的频率：")
    csort = sorted(cdict.keys())
    for cs in csort:
        print("{:<10}{:.2%}".format(cs,float(cdict[cs]/cnum)))
    #出现频率最高的单词
    wsort={}
    for key in wdict.keys():
        if wdict[key]>=4000:
            wsort[key]=wdict[key]    
    del wdict
    class1 = sorted(wsort.items(),key=lambda kv:(kv[1],kv[0]),reverse=True)
    print("文件中出现频率最高的十个单词及其出现次数:")
    n=0
    for x in class1 :
        n+=1
        if n==11:
            break
        print("{:<25}{:>10}".format(x[0],x[1]))

if __name__ == '__main__':
    main()
