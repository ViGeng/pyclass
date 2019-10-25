import project3_util as p


m=p.generate_exam_scores()

total = len(m)
print('总共%d同学分数如下:'%(total))
p.print_scores(m)

m.sort()

print('前10位分数(从高到低)分别为')
p.print_scores(m[total:total-11:-1])
print('后10位分数(从低到高)分别为')
p.print_scores(m[0:10:1])


def average():
    A=sum(m)/total
    print(float('%.1f' % A))


print('平均值:')
b=average()
