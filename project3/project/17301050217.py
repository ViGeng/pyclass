import random

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

def average_score(a_list):
    s = 0
    for i in a_list:
        s+=i
    average_score = s/len(a_list)
    return average_score


def main():
    exam_scores = generate_exam_scores()
    print('\n总共%d同学分数如下:' % len(exam_scores))
    print_scores(exam_scores)
    #打印所有同学分数
    front_examscores = sorted(exam_scores,reverse = True)
    print('\n前10位分数(从高到低)分别为')
    print_scores(front_examscores[:10])
    #打印前十位
    back_examscores = sorted(exam_scores)
    print('\n后10位分数(从低到高)分别为')
    print_scores(back_examscores[:10])
    #打印后十位
    ave_score = average_score(exam_scores)
    print('平均分%.1f' % ave_score)
    #打印平均分
    a = len(front_examscores)
    if a%2==0:
        mid_score_list = front_examscores[a//2-1:a//2]
        mid_score = average_score(mid_score_list)
    else:
        mid_score_list = front_examscores[a//2:a//2+1]
        mid_score = mid_score_list[0]
    print('中位数%.1f' % mid_score)
    #打印中位数
    

if __name__=='__main__':
    main()

    
    

































