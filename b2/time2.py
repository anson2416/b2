# coding=utf-8
import time
import object2
import datetime


TIME_ENUM = object2.enum(
    'MS:1 S:1000 MINUTE:60000 HOUR:360000 DAY:86400000', split_char=":")

TIME_PATTERN = object2.enum2(
    TIME_PATTERN = "%Y-%m-%d %H:%M:%S" ,
    TIME_PATTERN_SHORT = "%d/%m/%y %H:%M",
    DATE_FMT_0 = "%Y%m%d",
    DATE_FMT_1 = "%Y/%m/%d",
    DATE_FMT_2 = "%Y/%m/%d %H:%M:%S",
    DATE_FMT_3 = "%Y-%m-%d"
)

def get_timestamp_by_string(time_string , time_pattern):
    """translate time string to timestamp
        param:timestring:time string;
        param:timepattern:string time format
        return:float:timestamp
    """
    return time.mktime(time.strptime(time_string, time_pattern))

def timestamp_2_string(time_stamp , time_pattern):
    return time.strftime(time_pattern,time.localtime(time_stamp))

def get_now_timestamp():
    return time.time()

def get_day_begin(n = 0):
    return datetime.datetime.combine(
        datetime.date.today(), datetime.time.min)  + datetime.timedelta(days = n)

def get_day_end(n = 0):
    return datetime.datetime.combine(
        datetime.date.today(), datetime.time.max)  + datetime.timedelta(days = n)

def get_datetime_by_timestr(timestr,time_pattern):
    """translate time string to datetime
        param:timestr:time string;
        param:timepattern:time string format
        return:datetime
    """
    return datetime.datetime.fromtimestamp(get_timestamp_by_string(timestr,time_pattern))



if __name__ == "__main__":
    print get_timestamp_by_string("20160830",TIME_PATTERN.DATE_FMT_0)
    print timestamp_2_string(time.time() , TIME_PATTERN.DATE_FMT_0)
    print type(get_day_begin())
    print get_day_begin(n = -12)
    print get_datetime_by_timestr("20160830",TIME_PATTERN.DATE_FMT_0)
    print datetime.datetime.now() - get_datetime_by_timestr("19880820",TIME_PATTERN.DATE_FMT_0)
    a = (datetime.datetime.now() - get_datetime_by_timestr("19880820",TIME_PATTERN.DATE_FMT_0)).days
    print a / 365  ,  a % 365
