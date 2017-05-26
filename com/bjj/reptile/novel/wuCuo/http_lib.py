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
    s =  items[0].replace("<br />", "")\
        .replace("&nbsp;", "")\
        .replace("*", "")
    s = s.lower()

    s1 = s[:20]
    s2 = s[20:]
    print s
    print s1 + s2
    if s2.find("ps:"):
        return s1 + s2[:s2.index("ps:")]
    else:
        return s


def isPageError(index, title, url):

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = response.read().decode("gbk")
        pattern = re.compile('<div id="content">(.*?)</div>', re.S)
        items = re.findall(pattern, result)
        content = items[0].replace("<br />", "") \
            .replace("&nbsp;", "") \
            .replace("*", "")
        content = content.lower()
        if content.find("ps:"):
            content =  content[:content.index("ps:")]

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
