def sort_by_ID(item):
    return item['ID']

def sort_by_score(item):
    return item['score']

import project7_util as util
import random
import string

def main():
    names = []
    scores = []
    ids = []
    persons = []

    print('%3s     %-10s   %-3s'% ('ID', 'Name', 'Score'))

    i = 0
    t = 25
    while i < t:
        a = util.get_name(min_chars=3, max_chars=8)
        names.append(a)
        names = list(names)
        b = util.get_score()
        scores.append(b)
        scores = list(scores)
        c = util.get_id()
        ids.append(c)
        ids = list(ids)
        d = dict(zip(('ID', 'Name', 'score'), (c, a, b)))
        persons.append(d)
        persons = list(persons)
        i += 1

    persons2 = sorted(persons, key = sort_by_ID)
        
    m = 0
    while m < t:
        print('%3d     %-10s   %-3d'% (persons2[m]['ID'], persons2[m]['Name'], persons2[m]['score']))
        m += 1
        

    print()
    print('-' * 40)
    print()

    persons3 = sorted(persons2, key = sort_by_score)

    print('%3s     %-10s   %-3s'% ('ID', 'Name', 'Score'))

    n = 0
    while n < t:
        print('%3d     %-10s   %-3d'% (persons3[n]['ID'], persons3[n]['Name'], persons3[n]['score']))
        n += 1

if __name__ == "__main__":
    main()





