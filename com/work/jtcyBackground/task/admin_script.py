#! usr/bin/python
# coding:UTF-8

import sys
sys.path.append('..')
from core import apis
from task import user_script

"""
批量添加企业管理员
"""
def addAdmin(deptId, pageIndex, pageSize):
    li = user_script.getUserUidMobile(deptId, pageIndex, pageSize)
    for user in li:
        print apis.saveAdmin(user[0], user[1], 0).body

"""
批量添加其它管理员
deptIdList = [1, 2, 3, 4]
"""
def addAdmin1(deptId, pageIndex, pageSize, role, deptIdList):
    # role: 0=企业管理员 3=部门管理员 5=超级管理员 6=薪资管理员 7=考勤管理员 8=资费管理员
    li = user_script.getUserUidMobile(deptId, pageIndex, pageSize)
    for user in li:
        print apis.saveAdmin(user[0], user[1], role, deptIdList).body

"""
获取管理员手机号列表
"""
def getAdminMobile(role):
    # 获取管理员列表    role: 0=企业管理员 3=部门管理员 5=超级管理员 6=薪资管理员 7=考勤管理员 8=资费管理员
    adminInfo = apis.getAdminList(role).jBody
    li = []
    for info in adminInfo['data']:
        li.append(info['adminMobile'])
    return li

"""
删除全部的管理员
"""
def deleteAdmin(role):
    # 获取管理员列表    role: 0=企业管理员 3=部门管理员 5=超级管理员 6=薪资管理员 7=考勤管理员 8=资费管理员
    li = getAdminMobile(role)
    for mobile in li:
        print apis.deleteAdmin(mobile).body


if __name__ == '__main__':
    deleteAdmin(3)
