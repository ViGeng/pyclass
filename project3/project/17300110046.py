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

def get_median(data):
   exam_scores.sort()
   data = exam_scores
   size = len(exam_scores)
   if size % 2 == 0: 
      # 判断列表长度为偶数
      median = (data[size//2]+data[size//2-1])/2
   if size % 2 == 1: 
      # 判断列表长度为奇数
      median = data[(size-1)//2]
   return median

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    print_scores(exam_scores)

    # 你编写的代码放在后面

    exam_scores.sort(reverse=True)
    org_exam_scores=exam_scores
    high_scores=org_exam_scores[0:10]
    
    print('\n前10位分数(由高到低)分别为：')
    print_scores(high_scores)
    
    print('\n后10位分数(由低到高)分别为：')
    low_scores=org_exam_scores[-11:-1]
    low_scores.sort()
    print_scores(low_scores)
    
    average=(sum(exam_scores))/len(exam_scores)
    print()
    print('平均分%.1f' % average)

    median = get_median(exam_scores)
    print()
    print ('中位数%.1f' % median)
