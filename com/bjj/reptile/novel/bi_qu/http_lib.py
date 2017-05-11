# coding:utf8
import re
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

url1 = "http://www.i7wx.com/book/8/8294/"
url2 = "http://www.i7wx.com/book/8/8294/500741.html"



def getAllChapter(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result =  response.read().decode("gbk")
    pattern = re.compile('<li><a href="(.*?)">(.*?)</a></li>', re.S)
    items = re.findall(pattern, result)
    allChapter = []
    for item in items:
        allChapter.append(item)
    return allChapter

def getSingleChapterContent(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result =  response.read().decode("gbk")
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    items = re.findall(pattern, result)
    return items[0].replace("<br/>","").replace("&nbsp;","")
    # for item in items:
    #     print item.replace("<br/>","").replace("&nbsp;","")



if __name__ == '__main__':
    li1 = getAllChapter(url1)
    f = open("E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\bi_qu\\test.txt", "r+")
    i = 1
    for lis in li1:
        url3 = "http://www.i7wx.com/book/8/8294/" + lis[0]
        content = getSingleChapterContent(url3)
        # print "开始写入： " + lis[1]
        print i
        f.write(lis[1] + "\n")
        f.write(content + "\n")
        time.sleep(2)
        i+=1
    f.close()
    # content = getSingleChapterContent(url2)
    # f.write(content)
    # f.close()



