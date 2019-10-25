import  project3_util as util
util.generate_exam_scores()
if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

exam_scores.sort(reverse=True)

a=exam_scores[:10]
b=exam_scores[-1:-11:-1]

print()
print('前10位分数（从高到低）分别为')


count = 0
for i in a: 
    print(i, end='\t')
    count += 1
    if count % 5 == 0:
        print() 
if count % 5 != 0:
    print()

print()
print('后10位分数（从低到高）分别为')

count = 0
for i in b: 
    print(i, end='\t')
    count += 1
    if count % 5 == 0:
        print() 
if count % 5 != 0:
    print()

x=sum(exam_scores)
y=len(exam_scores)
z=x/y
print()
print('平均分','%.1f'%z)

input()

    
