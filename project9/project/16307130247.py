from project9_util import detect_encoding,nl_filename
text_file_path = 'fudan_history.txt'
encode = detect_encoding(text_file_path)

rf = open(nl_filename(text_file_path),'w', encoding= encode)
with open(text_file_path, 'r', encoding = encode) as f:
    line_number = 1
    for line in f:
        line_text = line.strip()
        if line_text == '':
            rf.write(line)
        else:
            rf.write(str(line_number)+'\t'+line_text+'\n')
            line_number +=1
