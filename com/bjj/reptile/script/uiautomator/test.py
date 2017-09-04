# coding:utf8
import time
import datetime

from uiautomator import device as d

def startTime():
    now = datetime.datetime.now()

    print now.strftime('%Y-%m-%d %H:%M:%S')
    return now

if __name__ == '__main__':
    t1 = startTime()
    time.sleep(13)
    t2 = startTime()

    print t2 - t1