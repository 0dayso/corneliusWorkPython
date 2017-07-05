#! usr/bin/python
# coding:UTF-8
import cookielib
import os
import urllib
import urllib2
import time

fileName = os.getcwd() + "\cookie.txt"
print fileName
cookie = cookielib.MozillaCookieJar(fileName)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdate = urllib.urlencode({
    "phone" : "14088888888",
    "code" : "1234"
})

url = "http://acl.admin.jituancaiyun.net/power/user/api/login.do"

result = opener.open(url, postdate)

cookie.save(ignore_discard=True, ignore_expires=True)
# for item in cookie:
#     print "Name = " + item.name
#     print "Value = " + item.value
url1 = "http://admin.jituancaiyun.net/entadmin/loginAdmin?orgId=571710020&orgName=%E9%9B%86%E5%9B%A2%E5%BD%A9%E4%BA%91%E6%B5%8B%E8%AF%95%E4%BC%81%E4%B8%9A020&_=1499053396702"
cookie.load(fileName, ignore_discard=True, ignore_expires=True)
req = urllib2.Request(url1)
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
response = opener.open(req)






