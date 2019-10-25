import project3_util as util
if __name__ == '__main__':
    exam_scores = util.generate_exam_scores()
    print('\n总共%d同学分数如下：' % len(exam_scores))
    util.print_scores(exam_scores)
    print("前10位分数(从高到低)分别为")
    util.print_scores(sorted(exam_scores,reverse = True)[:10])
    print("后10位分数(从低到高)分别为")
    util.print_scores(sorted(exam_scores,reverse = True)[-1:-11:-1])
    print("平均分",'%.1f'%(sum(exam_scores)/len(exam_scores)))
    
    


