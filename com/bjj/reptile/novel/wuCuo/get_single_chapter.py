# coding:utf8
import re
import urllib2

# url1 = "http://www.dawenxue.net/42082/11179069.html"

url1 = "http://www.dawenxue.net/2905/752274.html"


def getSingleChapterContent(url):
    request = urllib2.Request(url)
    response = urllib2.urlopen(request)
    print response.read()
    result = response.read().decode("gbk")
    # print result
    pattern = re.compile('<div id="content">(.*?)</div>', re.S)
    items = re.findall(pattern, result)
    print items[0]
    s = items[0].replace("<br />", "") \
        .replace("&nbsp;&nbsp;&nbsp;&nbsp;", "  \n") \
        .replace("*", "")
    s = s.lower()

    s1 = s[:20]
    s2 = s[20:]
    # print s
    # print s1 + s2
    if s2.find("ps:") != -1:
        return s1 + s2[:s2.index("ps:")]
    else:
        return s


if __name__ == '__main__':
    print getSingleChapterContent(url1)
