# coding:utf8
import re
import urllib2

url1 = "http://www.dawenxue.net/42082/11179069.html"


def getAllChapter(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result =  response.read().decode("gbk")
    print result


if __name__ == '__main__':
    getAllChapter(url1)
