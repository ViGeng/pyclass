import random

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


def generate_exam_scores():
    """ 某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    total = random.randint(45, 90)
    scores = []
    for i in range(total):
        scores.append(random.randint(50, 100))
    return scores

def main():
    scores = generate_exam_scores()
    num = len(scores)
    print('总共%2d同学分数如下'%(num))
    print_scores(scores)
    print()

    scores.sort()
    scoreslow = list(scores)
    scores.sort(reverse = True)
    scoreshigh = scores[:]
    a = list(scoreshigh)
    scoreshigh[:10]
    print('前10位分数（从高到低）分别为')
    print_scores(scoreshigh[:10])
    print()
    scoreslow[:10]
    print('后10位分数（从低到高）分别为')
    print_scores(scoreslow[:10])
    print()
    average = sum(scoreslow) / len(scoreslow)
    print('%3s%.1f' %('平均分',average))
    print()
    x = len(a) - 1
    x = x // 2
    y = len(a) - x
    a[x:y]
    scoresnew = a[x:y]
    middle = sum(scoresnew) / len(scoresnew)
    print('%3s%.1f' %('中位数',middle))

if __name__ == '__main__':
    main()

