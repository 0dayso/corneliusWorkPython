#! usr/bin/python
# coding:UTF-8


import cookielib
import os
import urllib
import urllib2
import time
import sys
sys.path.append("..")
from basic import config_file
# from com.work.jtcyBackground.common import config_file


fileName = 'E:\\workspace\\corneliusWorkPython\\com\\work\\jtcyBackground\\core\\cookie.txt'
cookie = cookielib.MozillaCookieJar(fileName)

def login():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdate = urllib.urlencode({
        "phone" : config_file.PHONE,
        "code" : "1234"
    })
    url = "http://acl.admin.jituancaiyun.net/power/user/api/login.do"

    opener.open(url, postdate)

    cookie.save(ignore_discard=True, ignore_expires=True)
    timestamp = str(int(time.time()*1000))

    url1 = "http://admin.jituancaiyun.net/entadmin/loginAdmin?orgId=%s&orgName=%s&_=%s"%(
        config_file.ORG_ID, urllib.quote(config_file.ORG_NAME), timestamp)

    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url1)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req)
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':
    login()





