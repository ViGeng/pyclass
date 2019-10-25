import random
def generate_exam_scores():
    """ 某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
total = random.randint(45, 90)
score = int(total)
scores = [random.randint(50, 100) for _ in range(score)]
print("总共%.f位同学成绩如下:" % score)
def print_scores(scores):
    """ 打印scores中的分数，每行5个数值"""
count = 0
for score in scores: 
    print(score, end='\t')
    count += 1
    if count % 5 == 0:
       print() 
if count % 5 != 0:
        print()
sum = 0
for i in scores:
    sum = sum + i
ave = sum / len(scores)
D = scores
def get_median(D):
    half = len(D) // 2
    return (D[half] + D[~half]) / 2
min = get_median(D)
C = sorted(scores)
print(" ")
print("前十位分数（从高到低）分别为")
C.sort(reverse=True)
scores = [];
score = 10
for i in range(score):
    scores.append(C[i]);
def print_scores(scores):
    """ 打印scores中的分数，每行5个数值"""        
count = 0
for score in scores: 
    print(score, end='\t')
    count += 1
    if count % 5 == 0:
       print() 
if count % 5 != 0:
        print()
print (" ")
print("后十位分数（从低到高）分别为")
C = D
C = sorted(D)
scores = [];
score = 10
for i in range(score):
    scores.append(C[i]);
def print_scores(scores):
    """ 打印scores中的分数，每行5个数值"""        
count = 0
for score in scores: 
    print(score, end='\t')
    count += 1
    if count % 5 == 0:
       print() 
if count % 5 != 0:
        print()
print(" ")
print("平均分%.1f" % ave)
print(" ")
print("中位数%.1f" % min)

