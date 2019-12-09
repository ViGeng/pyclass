def main():
    text=open("fudan_history.txt",encoding="GBK").read()
    lines=text.splitlines()
    new_text=[]
    t=0

    for i in range(len(lines)):
        if lines[i]!=("") and lines[i]!=(" "):
            t+=1
            line="%2d%s\n"%(t,lines[i])
            new_text.append(line)
        else:
            new_text.append("\n")

    open("new_fudan_history.txt",'w').writelines(new_text)

if __name__ == "__main__":
    main()
