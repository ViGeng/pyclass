import project3_util

exam_score = project3_util.generate_exam_scores()
sorted_exam_score = exam_score[:]
sorted_exam_score.sort()

def top_10(scores):
    top_score = scores[len(scores)-1:len(scores)-11:-1]
    print('前10位分数（从高到低）分别为')
    project3_util.print_scores(top_score)


def low_10(scores):
    low_score = scores[0:10]
    
    print('后10位分数（从低到高）分别为')
    project3_util.print_scores(low_score)
   

def mean_score(scores):
    totals_score = 0
    for i in scores:
        totals_score += i
        
    print('平均分%.1f'%(totals_score/len(scores)))


def median_score(scores):
    median1 = scores[len(scores)//2]
    median2 = scores[-(len(scores)//2)-1]
    print('中位数%.1f'%((median1+median2)/2))
        

if __name__ == '__main__':
    print('总共%s同学分数如下：'%(len(sorted_exam_score)))
    project3_util.print_scores(exam_score)
    print(' ')
    top_10(sorted_exam_score)
    print(' ')
    low_10(sorted_exam_score)
    print(' ')
    mean_score(exam_score)
    print(' ')
    median_score(sorted_exam_score)


