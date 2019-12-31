def main():
    with open('bill.txt') as f:
        text=f.read()
        num_str=len(text)
        num_line=len(text.splitlines())
        text_lower=text.lower()
        text_final=text_lower.replace('-\n\n','')
        words=text_final.split()
        num_word=0      
        char=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        dictory={}
        for l in words:
            for i in range(26):
                if l in dictory and char[i] in l:
                    dictory[l]+=1
                    num_word+=1
                    break
                if l not in dictory and char[i] in l:
                    dictory[l] =1
                    num_word+=1
                    break
##        for i in text.splitlines():
##            if i.endswith('-'):
##                num_word-=1
        
        times_char={}

        num_char=0
        for i in text_lower:
            if i in char:
                num_char+=1
        for j in text_lower:
            if j not in times_char and j in char:
                times_char[j]=1
            if j in times_char and j in char:
                times_char[j]+=1

        print('1.包含%d个字符，%d行，%d个单词'%(num_str,num_line,num_word))
        print('2.')
        for k in times_char:
            print('文件中%s出现的概率为%.2f%%'%(k,times_char[k]*100/num_char))
        print('3.出现频率最高的10个单词：')
        sorted_dict=sorted(dictory.items(),key=lambda item:item[1],reverse=True)
        for key,value in sorted_dict[:10]:
            print('%s : %d'%(key,value))
if __name__ == '__main__':
    main()
