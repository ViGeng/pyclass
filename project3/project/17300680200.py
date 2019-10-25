import project3_util as util

if __name__ =='__main__':
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)
    exam_total = list()
    for score in exam_scores:
        a = exam_total.append(score)

    b = exam_total.sort()
    first10 = exam_total[-1:-11:-1]
    last10 = exam_total[0:10]
    print()
    print('前10位分数（从高到低）分别为')
    util.print_scores(first10)
    print()
    print('后10位分数（从高到低）分别为')
    util.print_scores(last10)

    average = sum(exam_total)/len(exam_total)
    print()
    print('%3s%4.1f' %('平均分',average))

    if len(exam_total) % 2 ==1:
        middle = int((len(exam_total) - 1)/ 2)
        middle_score = exam_total[middle]
        print('%3s%-4.1f'%('中位分',middle_score))
    else:
        middle1 = int((len(exam_total))/ 2)
        middle2 = int((len(exam_total))/ 2 - 1)
        middle_score = (exam_total[middle1] + exam_total[middle2]) / 2
        print('%3s%-4.1f'%('中位分',middle_score))
