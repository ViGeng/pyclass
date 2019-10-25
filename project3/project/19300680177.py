import project3_util as util

if __name__ == '__main__':
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下:'%len(exam_scores))
    util.print_scores(exam_scores)
    exam_scores.sort()
    a=exam_scores


    average = sum(exam_scores)/len(exam_scores)
    print()


    print("前10位分数（从高到低）分别为")
    util.print_scores(exam_scores[-1:-11:-1])
    
    print("\n后10位分数（从低到高）分别为")
    util.print_scores(exam_scores[0:10])

    print("\n平均分%.1f"%average)
