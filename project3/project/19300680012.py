from project3_util import *
if __name__ == '__main__':
    scores=generate_exam_scores()
    print("总共%d同学分数如下："%len(scores))
    print_scores(scores)
    scores.sort()
    a=sum(scores)/len(scores)

    if len(scores)%2==0:
        x=(scores[len(scores)//2-1]+scores[len(scores)//2])/2
    else:
        x=scores[(len(scores)-1)//2]

    print()
    print("前10名的分数(从高到低)分数为")
    print_scores(scores[-1:-11:-1])
    print("后10名的分数(从低到高)分数为")
    print_scores(scores[0:10])
    print()
    print("平均分%.1f"%a)
    print()
    print("中位数%.1f"%x)
