#! usr/bin/python
# coding:UTF-8
import re
import urllib2



text = "E:\\workspace\\corneliusWorkPython\\com\\bjj\\reptile\\novel\\bi_qu\\test.txt"
f = open(text, "r+")


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
    if index<5:
      index+=1
      isPageError(index, title, url)
  return False



if __name__ == '__main__':
    print isPageError(1,"123", "http://www.baidu.com")








































