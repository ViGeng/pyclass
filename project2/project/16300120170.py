import project2_util



def get_time():
    
    import time
    current = time.localtime()
    return  current.tm_hour, current.tm_min

def test_datetime():
    import datetime
    now = datetime.datetime.now()
    print('当前时间%02d:%02d' % (now.hour, now.minute))
    

     



if __name__ == '__main__':    
#    wday,hour,minute = get_time()
#    print(wday, hour, minute)

    test_datetime()
    



       


