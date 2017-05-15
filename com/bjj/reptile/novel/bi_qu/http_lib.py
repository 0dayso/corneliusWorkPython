# coding:utf8
import re
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

url1 = "http://www.i7wx.com/book/8/8294/"
url2 = "http://www.i7wx.com/book/8/8294/500741.html"
text = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\bi_qu\\test.txt"
error = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\bi_qu\\error.txt"

f = open(text, "r+")
f1 = open(error, "r+")





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
    result = response.read().decode("gbk")
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    items = re.findall(pattern, result)
    return items[0].replace("<br/>", "").replace("&nbsp;", "")

def isPageError(index, title, url):

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = response.read().decode("gbk")
        pattern = re.compile('<div id="content">(.*?)</div>', re.S)
        items = re.findall(pattern, result)
        content = items[0].replace("<br/>", "").replace("&nbsp;", "")
        f.write(title + "\n")
        f.write(content + "\n")
    except Exception, e:
        print Exception, ":", e
        index+=1
        if index<5:
            isPageError(index, title, url)
    return False





if __name__ == '__main__':
    li1 = getAllChapter(url1)
    i = 1
    for lis in li1:
        url3 = "http://www.i7wx.com/book/8/8294/" + lis[0]
        try:
            content1 = getSingleChapterContent(url3)
            # print "开始写入： " + lis[1]
            print i
            f.write(lis[1] + "\n")
            f.write(content1 + "\n")
            time.sleep(2)
            i+=1
        except Exception, e:
            print Exception, " : ", e
            if not isPageError(1, lis[1], url3):
                f1.write("[\"" + lis[0] + "\",[\"" + lis[1] + "\"],")

    f.close()
    f1.close()
    # content = getSingleChapterContent(url2)
    # f.write(content)
    # f.close()



