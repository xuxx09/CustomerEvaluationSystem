import datetime
import time


def time2stamp(timestr, format_type='%Y-%m-%d'):
    return time.mktime(time.strptime(timestr, format_type))


def stamp2time(stamp, format_type='%Y-%m-%d'):
    return time.strftime(format_type, time.localtime(stamp))


def delt2time(delt=30):
    deltDate = datetime.datetime.now() + datetime.timedelta(days=-delt)
    #print deltDate
    timeStamp = time.mktime(deltDate.timetuple())
    return timeStamp

    
def default_end_time():
    stamp = time.time()
    return stamp2time(stamp)


    
def default_begin_time():
    stamp = delt2time()
    return stamp2time(stamp)


if __name__ == '__main__':
    '''
    this is the test function
    '''

    
    stamp = time.time()
    print stamp2time(stamp)
    print time2stamp(nowtime)
    print delt2time()
    print delt2time(7)
    print default_begin_time()
    print default_end_time()

    
    
