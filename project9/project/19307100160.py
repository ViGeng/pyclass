from project9_util import detect_encoding,nl_filename
text = 'fudan_history.txt'
encode = detect_encoding(text)

rf = open(nl_filename(text),'w', encoding= encode)
with open(text, 'r', encoding = encode) as f:
    count = 1
    for line in f:
        line_text = line.strip()
        if line_text == '':
            rf.write(line)
        else:
            rf.write(str(count)+'\t'+line_text+'\n')
            count +=1
