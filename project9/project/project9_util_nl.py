    1	#!/usr/bin/env python3
    2	#  -*- coding: utf-8 -*-
    3	""" project 9 给文件加上行号
    4	"""

    5	def detect_encoding(text):
    6	    """探测文件的编码方式
    7	    参数：文件名， 返回探测到的编码方式
    8	    """

    9	    # UTF-8-SIG
   10	    encodings = 'ASCII'   11	 'UTF-8'   12	 'GBK'

   13	    for encoding in encodings:
   14	        try:
   15	            with open(text   16	 encoding=encoding) as f:
   17	                f.read(100)
   18	            break
   19	        except UnicodeDecodeError:
   20	            pass
   21	    return encoding


   22	def nl_filename(name):
   23	    """ 返回一个新的文件名，传递的参数name为文件名
   24	    """

   25	    if name.endswith(('.txt'   26	 '.py')):
   27	        dot_pos = name.rindex('.')
   28	        return name[0:dot_pos] + '_nl' + name[dot_pos:]
   29	    else:
   30	        return name + '_nl'

   31	if __name__ == '__main__':
   32	    print('%s-->%s: %s' % (__file__   33	 nl_filename(__file__)   34	 detect_encoding(__file__)))

   35	    text = 'fudan_history.txt'
   36	    print('%s-->%s: %s' % (text   37	 nl_filename(text)   38	 detect_encoding(text)))1 #!/usr/bin/env python3
2 #  -*- coding: utf-8 -*-
3 """ project 9 给文件加上行号
4 """

5 def detect_encoding(text):
6     """探测文件的编码方式
7     参数：文件名， 返回探测到的编码方式
8     """

9     # UTF-8-SIG
10     encodings = 'ASCII', 'UTF-8', 'GBK'

11     for encoding in encodings:
12         try:
13             with open(text, encoding=encoding) as f:
14                 f.read(100)
15             break
16         except UnicodeDecodeError:
17             pass
18     return encoding


19 def nl_filename(name):
20     """ 返回一个新的文件名，传递的参数name为文件名
21     """

22     if name.endswith(('.txt', '.py')):
23         dot_pos = name.rindex('.')
24         return name[0:dot_pos] + '_nl' + name[dot_pos:]
25     else:
26         return name + '_nl'

27 if __name__ == '__main__':
28     print('%s-->%s: %s' % (__file__, nl_filename(__file__), detect_encoding(__file__)))

29     text = 'fudan_history.txt'
30     print('%s-->%s: %s' % (text, nl_filename(text), detect_encoding(text)))