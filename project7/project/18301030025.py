
import random
import string

def get_name(min_chars=3, max_chars=8):
    """ 返回一个名字，长度介于min_chars和max_chars之间
    """
    VALID_CHARS = string.ascii_lowercase

    names = [random.choice(VALID_CHARS) for i in range(random.randint(min_chars,max_chars))]
    names[0] = names[0].upper()
    return ''.join(names)
def make_random_list1(limit=25):
    result = []
    while len(result) < limit:
        r = get_name(min_chars=3, max_chars=8)
        if r not in result:
            result.append(r)
    return result
result1= make_random_list1(limit=25)

def get_score():
    """ 返回一个分数，介于50和100之间
    """
    return random.randint(50,100)
def make_random_list1(limit=25):
    result = []
    while len(result) < limit:
        r = get_score()
        if r not in result:
            result.append(r)
    return result
result2= make_random_list1(limit=25)

ids_in_use = []
def get_id():
    """ 返回一个唯一的ID，在[1,999]之间
    """
    global ids_in_use   

    while True:
        s_id = random.randint(1, 999)
        if s_id not in ids_in_use:
            ids_in_use.append(s_id)
            return s_id
def make_random_list1(limit=25):
    result = []
    while len(result) < limit:
        r = get_id()
        if r not in result:
            result.append(r)
    return result
result3= make_random_list1(limit=25)
value1 = {k:[v,t]  for k,v,t in zip(result3,result1,result2)}

value3=sorted(value1.items(),key=lambda d:d[1][1])


print('成绩单如下，按照ID排序\n')
print('   ID   name     Score')
def fn(value1):
    lis = [[x,value1[x]] for x in value1]
    return lis
result = fn(value1)
value2 = sorted(zip(result3,result1,result2))
for val in iter(value2):
    print('%5s  %-8s  %2d' % val)
    
        
print()
print('-'*50)
print()
print('成绩单如下，按照成绩排序\n')
print('  ID    name     Score')
for val in iter(value3):
        print(val)
  
        
    



