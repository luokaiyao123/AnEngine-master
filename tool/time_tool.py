import datetime


def get_local_datestr():
    """返回当前日期格式"""
    return datetime.datetime.now().strftime('%Y-%m-%d')

def get_local_timestr():
    """返回当前时间格式"""
    return datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

if __name__ == '__main__':
    print(get_local_timestr())
