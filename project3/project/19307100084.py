import project3_util as util


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

ambro=sorted(exam_scores)
descending_scores=reversed(ambro)
acsending_scores=sorted(exam_scores)

def print_tops(tops):
    """打印tops中的分数，每行5个数值"""
    count = 0
    for top in tops:
            print(top,end='\t')
            count += 1
            if count == 5:
                print()
            if count == 10:
                break
            
print('前10位分数(从高到低)分别为:')
print_tops(descending_scores)
print()
print('前10位分数(从低到高)分别为:')
print_tops(acsending_scores)

a=sum(exam_scores)/len(exam_scores)
print()
print('平均分：')
print(a)

def print_medium(exam_scores):
    exam_scores.sort()
    final=len(exam_scores)//2
    return(exam_scores[final]+exam_scores[-final])/2

print()
print('中位数：')
print(print_medium(exam_scores))

