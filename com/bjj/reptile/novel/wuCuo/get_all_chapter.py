#! usr/bin/python
# coding:UTF-8

import re
import urllib2

# url1 = "http://www.dawenxue.net/8613/"
url1 = "http://www.dawenxue.net/49807/" #大明最后一个太子

text1 = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\wuCuo\\allChapter.txt"

f2 = open(text1, "r+")

def getAllChapter(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    result =  response.read()
    # result =  response.read().decode("gbk")
    pattern = re.compile('<dd><a href="(.*?)">(.*?)</a></dd>', re.S)
    items = re.findall(pattern, result)
    allChapter = []
    for item in items:
        # s = item[1]
        # if s.startswith("第"):
        #     allChapter.append(item)
        f2.write(item[0] + "," + item[1] + "\n")

    # for chapter in allChapter:
    #     print chapter
    #     f2.write(chapter[0] + ", " + chapter[1] + "\n")
    f2.close()

if __name__ == '__main__':
    getAllChapter(url1)
