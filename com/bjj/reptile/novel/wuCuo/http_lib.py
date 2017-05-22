# coding:utf8
import re
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

url1 = "http://www.dawenxue.net/42082/"
url2 = "http://www.i7wx.com/book/8/8294/500741.html"
text = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\text.txt"
error = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\error.txt"
text1 = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\error1.txt"


f = open(text, "r+")
f1 = open(error, "r+")
f2 = open(text1, "r+")





def getAllChapter():
    request = urllib2.Request("http://www.dawenxue.net/42082/")
    response = urllib2.urlopen(request)
    result =  response.read().decode("gbk")
    pattern = re.compile('<dd><a href="(.*?)">(.*?)</a></dd>', re.S)
    items = re.findall(pattern, result)
    allChapter = []
    for item in items:
        s = item[1]
        if s.startswith("第"):
            allChapter.append(item)

    for chapter in allChapter:
        print chapter
        f2.write(chapter[0] + ", " + chapter[1] + "\n")
    f2.close()

def getSingleChapterContent(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result = response.read().decode("gbk")
    print result
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    items = re.findall(pattern, result)
    return items[0].replace("<br />", "")\
        .replace("&nbsp;", "")\
        .replace("*", "")\
        .replace("PS：朋友们，新书正式上传喽！新的征程，愿与各位并肩同行。点击、收藏、推荐，你的每一点支持，都是我前进的动力！.手机用户请到m.qidian.com阅读。","")\
        .replace("PS：亲们，看完书别忘了收藏啊，另外顺手扔下几张推荐票，支持一下新书，支持一下昊远，好人一生平安！.手机用户请到m.qidian.com阅读。","")


def isPageError(index, title, url):

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = response.read().decode("gbk")
        pattern = re.compile('<div id="content">(.*?)</div>', re.S)
        items = re.findall(pattern, result)
        content = items[0].replace("<br />", "") \
            .replace("&nbsp;", "") \
            .replace("*", "") \
            .replace("PS：朋友们，新书正式上传喽！新的征程，愿与各位并肩同行。点击、收藏、推荐，你的每一点支持，都是我前进的动力！.手机用户请到m.qidian.com阅读。","")\
            .replace("PS：亲们，看完书别忘了收藏啊，另外顺手扔下几张推荐票，支持一下新书，支持一下昊远，好人一生平安！.手机用户请到m.qidian.com阅读。","")


        f.write(title + "\n")
        f.write(content + "\n")
    except Exception, e:
        print Exception, ":", e
        index+=1
        if index<5:
            isPageError(index, title, url)
    return False





if __name__ == '__main__':

    lines = f2.readlines()
    for line in lines:
        line = line.split(",")
        print line[0]
        url3 = "http://www.dawenxue.net/42082/" + line[0]
        print url3 + "  " + line[1]

        try:
            content1 = getSingleChapterContent(url3)
            # print "开始写入： " + lis[1]
            f.write(line[1] + "\n")
            f.write(content1 + "\n")
            time.sleep(1)
        except Exception, e:
            print Exception, " : ", e
            if not isPageError(1, line[1], url3):
                f1.write(line[0] + "," + line[1] + "\n")


    f2.close()
    f.close()
    f1.close()
    # content = getSingleChapterContent(url2)
    # f.write(content)
    # f.close()
