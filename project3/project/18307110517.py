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


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    print_scores(exam_scores)
    print()


exam_scores.sort(reverse=True)
print('前10位分数(从高到低)分别为')
print_scores(exam_scores[:10:1])
print()
print('后10位分数(从低到高)分别为')
print_scores(exam_scores[:-11:-1])
print()


def average(exam_scores):
    sum_scores=0
    for i in range(len(exam_scores)):
        sum_scores += exam_scores[i]
    return sum_scores / len(exam_scores)


print('平均分','%.1f'%average(exam_scores))
print()


def median(exam_scores):
    len_scores = len(exam_scores)
    if len_scores % 2 == 1:
        i = int((len_scores + 1) / 2)-1
        return exam_scores[i]
    else:
        i = int(len_scores/ 2)-1
        return (exam_scores[i] + exam_scores[i + 1]) / 2


print('中位数','%.1f'%median(exam_scores))

