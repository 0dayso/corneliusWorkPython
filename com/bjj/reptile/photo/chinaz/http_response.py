#! usr/bin/python
# coding:UTF-8
import re
import urllib2
import time

name = 'chiqiangdongzuotupian'
pages = 7

def getResponse(url):
    headers = {
        'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
        'Referer' : 'http://sc.chinaz.com/tupian'
    }
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)
    time.sleep(3)
    return response.read()

def getDownloadUrl(url):
    html = getResponse(url)
    pattern = re.compile('<div>.*?alt="(.*?)"><img src2="(.*?)" alt=.*?</div>', re.S)
    items = re.findall(pattern, html)
    allUrl = []
    for item in items:
        ss = item[1]
        if 'pic.sc.chinaz.com/Files/pic/' in ss:
            ss = ss.replace('pic.sc.chinaz.com/Files/pic/', 'zjyd.sc.chinaz.com/Files/DownLoad/')
        elif 'pic1.sc.chinaz.com/Files/pic/' in ss:
            ss = ss.replace('pic1.sc.chinaz.com/Files/pic/', 'zjyd.sc.chinaz.com/Files/DownLoad/')
        elif 'pic2.sc.chinaz.com/Files/pic/' in ss:
            ss = ss.replace('pic2.sc.chinaz.com/Files/pic/', 'zjyd.sc.chinaz.com/Files/DownLoad/')
        ss = ss[:-6] + '.rar'
        item1 = (item[0], ss)
        allUrl.append(item1)
    return allUrl

def writeToTxt(url):
    allUrl = getDownloadUrl(url)
    f = open('D:\\test\\chinaz\\%s.txt'%name, 'a+')
    for item in allUrl:
        bu = item[0] + ', ' + item[1] + '\n'
        f.write(bu)
    f.close()

if __name__ == '__main__':
    for i in range(1, pages + 1):
        print "开始" + str(i) + "次请求"
        if i == 1:
            mainUrl = "http://sc.chinaz.com/tupian/%s.html"%name
            writeToTxt(mainUrl)
        else:
            mainUrl = "http://sc.chinaz.com/tupian/%s_%s.html"%(name, i)
            writeToTxt(mainUrl)