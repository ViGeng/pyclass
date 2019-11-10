def _oula():
    i=m=sigle_item=1
    total = 1
    while sigle_item>=10**-10:
        m *= i
        sigle_item = 1/m
        total += sigle_item
        i += 1

    return total


if __name__ == '__main__':
   print(_oula())
