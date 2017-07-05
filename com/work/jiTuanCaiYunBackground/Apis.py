#! usr/bin/python
# coding:UTF-8
import cookielib
import json
import os
import time
import urllib
import urllib2
import config
from urllib import urlencode


fileName = os.getcwd() + "\\cookie.txt"
cookie = cookielib.MozillaCookieJar(fileName)

def login():
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    postdate = urlencode({
        "phone" : config.PHONE,
        "code" : "1234"
    })
    url = "http://acl.admin.jituancaiyun.net/power/user/api/login.do"

    opener.open(url, postdate)

    cookie.save(ignore_discard=True, ignore_expires=True)
    timestamp = str(int(time.time()*1000))

    url1 = "http://admin.jituancaiyun.net/entadmin/loginAdmin?orgId=%s&orgName=%s&_=%s"%(config.ORG_ID, urllib.quote(config.ORG_NAME), timestamp)

    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url1)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req)
    cookie.save(ignore_discard=True, ignore_expires=True)

"""
获取部门列表信息
deptId: 部门id
"""
def getDeptDetailList(deptId):
    timestamp = str(int(time.time()*1000))
    url = "http://admin.jituancaiyun.net/entadmin/contact/dept?parentId=%s&_=%s"%(deptId,timestamp)
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    result = opener.open(req)
    return result

"""
获取部门人员信息
deptId : 部门Id
pageIndex : 从第几页人开始
pageSize : 请求多少个人
"""
def getUsers(deptId, pageIndex, pageSize):
    timestamp = str(int(time.time()*1000))
    url = "http://admin.jituancaiyun.net/entadmin/contact/dept/users?deptId=%s&pageIndex=%s&pageSize=%s&_=%s"%(deptId, pageIndex, pageSize, timestamp)
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    return opener.open(req)

def batchDelUser(li):
    url = "http://admin.jituancaiyun.net/entadmin/batchDelUser"
    # data = urlencode({
    #     'userIds' : li
    # })
    data = {
        'userIds' : li
    }
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url, json.dumps(data))

    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req)

def saveUser(departmentId, isallowlogin, mobile, name, sequence, email=None, fax=None, homePhone=None, id=None,
             jobCode=None, oldDepartmentId=None, oldIsallowlogin=None, oldMobile=None, oldPrivgroup=None,
             oldSequence=None, privgroup=None, privilege=None, shortNum=None, shortNum2=None, title=None, uid=None,
             virtualCellPhone=None, virtualCode=None, workPhone=None, workPhone2=None):
    url = "http://admin.jituancaiyun.net/entadmin/saveUser"
    data = urlencode({
        "customFieldString" : "",
        "departmentId" : departmentId,
        "email" : email,
        "fax" : fax,
        "homePhone" : homePhone,
        "id" : id,
        "isallowlogin" : isallowlogin,
        "jobCode" : jobCode,
        "mobile" : mobile,
        "name" : name,
        "oldDepartmentId" : oldDepartmentId,
        "oldIsallowlogin" : oldIsallowlogin,
        "oldMobile" : oldMobile,
        "oldPrivgroup" : oldPrivgroup,
        "oldSequence" : oldSequence,
        "privgroup" : privgroup,
        "privilege" : privilege,
        "sequence" : sequence,
        "shortNum" : shortNum,
        "shortNum2" : shortNum2,
        "title" : title,
        "uid" : uid,
        "virtualCellPhone" : virtualCellPhone,
        "virtualCode" : virtualCode,
        "workPhone" : workPhone,
        "workPhone2" : workPhone2
    })
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req, data)

def saveDept(deptName, sequence, parentId, oldSequence=None, oldParentId=None, id=None, isJudgeExist=True):
    url = "http://admin.jituancaiyun.net/entadmin/contact/dept/save"
    data = urlencode({
        "name" : deptName,
        "sequence" : sequence,
        "oldSequence" : oldSequence,
        "parentId" : parentId,
        "oldParentId" : oldParentId,
        "id" : id,
        "judgeExist" : isJudgeExist,
        "uids" : []
    })

    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url, data)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    opener.open(req).read()

def deleteDept(deptId):
    url = "http://admin.jituancaiyun.net/entadmin/contact/dept/delete"
    headers ={
        "User-agent":"Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1"}
    data = urlencode({
        "id" : deptId
    })
    # data = {
    #     "id" : deptId
    # }
    cookie.load(fileName, ignore_discard=True, ignore_expires=True)
    req = urllib2.Request(url)
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
    print opener.open(req, data, headers).read()

if __name__ == '__main__':
    login()
    # print getDeptDetailList(0).read()
    # print saveDept("123", 4, 0, oldSequence=0,isJudgeExist=False)
    # print saveUser(departmentId=0, isallowlogin=True, mobile="14000001547", name="imya", sequence=1)
    # deleteDept(1)
