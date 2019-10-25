import project3_util as util


if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

vante=sorted(exam_scores)

vante[:10]=[]

descending_scores = reversed(vante)

amor = sorted(exam_scores)

amor[10:]=[]

acsending_scores = sorted(amor)




def print_lines(lines):
    """打印lines中的分数，每行5个数值"""
    count = 0
    for line in lines:
        print(line, end='\t')
        count += 1
        if count == 5 :
            print()
        if count == 10:
            break

print('前10位分数（从高到低）分别为：')
print_lines(descending_scores)
print()
print('后10位分数 (从低到高) 分别为：')
print_lines(acsending_scores)
print()
average = sum(exam_scores)/len(exam_scores)
print('平均分：' , round(average,1) )
            



