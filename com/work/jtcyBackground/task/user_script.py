#! usr/bin/python
# coding:UTF-8

import sys
sys.path.append('..')
from core import apis
from core import basicMethod

"""
获取指定部门下的人员id
return '128','129','130','131','132'
"""
def getUserId(deptId, pageIndex, pageSize):
    resp = apis.getUsers(deptId, pageIndex, pageSize)
    resp = resp.jBody
    li = []
    for user in resp['data']['users']:
        li.append(str(user['id']))
    st = ",".join(li)
    return st

"""
获取指定部门下的人员uid和mobile
return [[902457, '14000015338'], [882641, '14000010384'], [101010012334104L, '14000011017']]
"""
def getUserUidMobile(deptId, pageIndex, pageSize):

    resp = apis.getUsers(deptId, pageIndex, pageSize)
    resp = resp.jBody
    li = []
    for user in resp['data']['users']:
        li1 = [user['uid'], user['mobile']]

        li.append(li1)
    return li

"""
删除指定部门人员
"""
def deleteUser(deptId, pageIndex, pageSize):
    st = getUserId(deptId, pageIndex, pageSize)
    re = apis.deleteUser(st)
    print re.body

"""
添加人员
"""
def addUser(deptId,nums):
    for i in range(nums):
        name = basicMethod.randomName()
        mobile = basicMethod.randomMobile()
        print apis.saveUser(name, deptId, mobile, i+1, True).body



if __name__ == '__main__':
    print getUserUidMobile(0,1,10)
