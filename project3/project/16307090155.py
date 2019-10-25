#导入模块
import project3_util as util

if __name__ == '__main__':
    """ 下面一段代码给出了某个班的某次考试的分数情况，保存在列表scores中。
    该班的人数随机产生，在[45,90]之间。某次考试的分数也是随机产生，
    分数值位于[50,100]之间。
    """
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)

if __name__== '__main__':
    print()

print(' ' * 30)
scores = util.generate_exam_scores()

#前10名
scores = sorted(scores,reverse = True)#ture,由大到小排列
print("前10位分数（从高到低）分别为")
util.print_scores(scores[0:10])#模块中公式

#后10名。第二种方法，更简便，问题：为什么需要写-11？
#print("后10位分数（从低到高）分别为")
#util.print_scores(scores[-1:-11:-1])#a-start;b-stop;c-步长


#后10名-第一种方式
print(' ' * 30)     
scores = sorted(scores,reverse = False)
print("后10位分数（从低到高）分别为" )
util.print_scores(scores[0:10])


#平均分
print(' ' * 30)
Average = sum(scores)/len(scores)
print("平均分 %.1f" % Average)

#中位数
print(' ' * 30)
size = len(scores)
if size % 2 == 0:#偶数时
    Median = (scores[size//2]+ scores[size//2-1])/2#"//"向下取整。？

if size % 2 == 1:#奇数时
    Median =scores[(size - 1)//2]
    
print("中位数 %.1f" % Median)


print(' ' * 30)
if __name__== '__main__':
    print()
