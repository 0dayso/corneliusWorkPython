# coding:utf8
import re
import urllib2
import sys
import time

reload(sys)
sys.setdefaultencoding('utf-8')

# url1 = "http://www.dawenxue.net/8613/"
url1 = "http://www.dawenxue.net/55425/"
text = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\text.txt"
error = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\error.txt"
text1 = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\allChapter.txt"


f = open(text, "r+")
f1 = open(error, "r+")
f2 = open(text1, "r+")

def getSingleChapterContent(url, title):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result = response.read()
    # result = response.read().decode("gbk")
    # print result
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    items = re.findall(pattern, result)
    s =  items[0].replace("<br />", "") \
        .replace("&nbsp;&nbsp;&nbsp;&nbsp;", "    \n") \
        .replace("*", "")
    s = s.lower()

    s1 = s[:100]
    s2 = s[100:]
    # print s
    # print s1 + s2
    if s1.find(title.strip()) != -1:
        s1.replace(title.strip(), "")

    if s2.find("ps:") != -1:
        return s1 + s2[:s2.index("ps:")]
    else:
        return s


def isPageError(index, title, url):

    try:
        request = urllib2.Request(url)
        response = urllib2.urlopen(request)
        result = response.read()
        # result = response.read().decode("gbk")
        pattern = re.compile('<div id="content">(.*?)</div>', re.S)
        items = re.findall(pattern, result)
        content = items[0].replace("<br />", "") \
            .replace("&nbsp;&nbsp;&nbsp;&nbsp;", "    \n") \
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
    i = 0
    for line in lines:
        line = line.split(",")
        # print line[0]
        url3 = url1 + line[0]
        print url3 + "  " + line[1]
        # print url3 + "  " + line[1].decode("gbk")

        try:
            content1 = getSingleChapterContent(url3, line[0])
            # print "开始写入： " + lis[1]
            f.write(line[1])
            f.write(content1 + "\n")
            time.sleep(1)
        except Exception, e:
            print Exception, " : ", e
            if not isPageError(1, line[1], url3):
                f1.write(line[0] + "," + line[1] + "\n")
        # i+=1
        # if i == 2:
        #     break


    f2.close()
    f.close()
    f1.close()

    # getAllChapter(url1)
