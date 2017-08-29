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
    if config_file.IS_ON_LINE:
        postdate = urllib.urlencode({
            "phone" : raw_input("请输入手机号:").replace(" ", ""),
            "code" : raw_input("请输入验证码:").replace(" ", ""),
        })
        url = "https://acl.admin.jituancaiyun.com/power/user/api/login.do"
    else:
        postdate = urllib.urlencode({
            "phone" : config_file.PHONE,
            "code" : "1234"
        })
        url = "http://acl.admin.jituancaiyun.net/power/user/api/login.do"

    opener.open(url, postdate)

    cookie.save(ignore_discard=True, ignore_expires=True)
    timestamp = str(int(time.time()*1000))

    if config_file.IS_ON_LINE:
        url1 = "https://admin.jituancaiyun.com/entadmin/loginAdmin?orgId=%s&orgName=%s&_=%s"%(
            config_file.ORG_ID_ON_LINE, urllib.quote(config_file.ORG_NAME_ON_LINE), timestamp)
    else:
        url1 = "http://admin.jituancaiyun.net/entadmin/loginAdmin?orgId=%s&orgName=%s&_=%s"%(
            config_file.ORG_ID, urllib.quote(config_file.ORG_NAME), timestamp)

    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url1)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req)
    cookie.save(ignore_discard=True, ignore_expires=True)

if __name__ == '__main__':
    login()





