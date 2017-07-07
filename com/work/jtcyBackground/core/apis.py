#! usr/bin/python
# coding:UTF-8
import time
import sys
sys.path.append('..')
from core import http_lib


def getDepartments(parenId):
    """
    获取部门下的部门列表
    :param parenId:父部门ID
    :return:
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept?parentId=%s&_=%s" % (parenId, timestamp)
    }
    return http_lib.http(args)

def saveDept(deptName, sequence, parentId, oldSequence=None, oldParentId=None, isJudgeExist=None):
    """
    创建部门
    """
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept/save",
        'data': {
            "name": deptName,   # 部门名称，必填
            "sequence": sequence,   # 部门排序，必填
            "oldSequence": oldSequence, # 老的部门排序
            "parentId": parentId, # 上级部门，必填 如果是一级部门则传0
            "oldParentId": oldParentId, # 老的父部门
            "id": None,
            "judgeExist": isJudgeExist, # 是否自动创建部门
            "uids": []
        }
    }
    return http_lib.http(args)

def deleteDept(deptId):
    """
    删除部门
    :param deptId: 删除部门的ID
    :return:
    """
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept/delete",
        'data' : {
            "id" : deptId
        }
    }
    return http_lib.http(args)

def getUsers(deptId, pageIndex, pageSize):
    """
    获取人员列表
    :param deptId: 要获取部门人员的部门ID
    :param pageIndex: 从第几页开始
    :param pageSize: 每页多少人
    :return:
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept/users?deptId=%s&pageIndex=%s&pageSize=%s&_=%s" % (
        deptId, pageIndex, pageSize, timestamp)
    }
    return http_lib.http(args)

def deleteUser(userIds):
    """
    删除人员
    """
    args = {
        'url' : '/entadmin/batchDelUser',
        'data' : {
            'userIds' : userIds # 参数样式：'128','129','130','131','132'
        }
    }
    return http_lib.http(args)

def saveUser(name, departmentId, mobile, sequence, isAllowLogin, customFieldString=None, email=None, fax=None, homePhone=None,
             jobCode=None, oldDepartmentId=None, oldIsallowlogin=None, oldMobile=None,
             oldPrivgroup=None, oldSequence=None, privgroup=None, privilege=None, shortNum=None, shortNum2=None,
             title=None, virtualCellPhone=None, virtualCode=None, workPhone=None, workPhone2=None):
    """
    创建人员
    """
    args = {
        'url' : "http://admin.jituancaiyun.net/entadmin/saveUser",
        'data' : {
            "name" : name,
            "mobile" : mobile,
            "departmentId" : departmentId,
            "sequence" : sequence,
            "isallowlogin" : isAllowLogin,

            # "customFieldString" : customFieldString,
            # "email" : email,
            # "fax" : fax,
            # "homePhone" : homePhone,
            # "id" : id,

            # "jobCode" : jobCode,
            # "oldDepartmentId" : oldDepartmentId,
            # "oldIsallowlogin" : oldIsallowlogin,
            # "oldMobile" : oldMobile,
            # "oldPrivgroup" : oldPrivgroup,
            # "oldSequence" : oldSequence,
            # "privgroup" : privgroup,
            # "privilege" : privilege,
            # "shortNum" : shortNum,
            # "shortNum2" : shortNum2,
            # "title" : title,
            # "uid" : None,
            # "virtualCellPhone" : virtualCellPhone,
            # "virtualCode" : virtualCode,
            # "workPhone" : workPhone,
            # "workPhone2" : workPhone2
        }
    }
    return http_lib.http(args)

def saveAdmin(uid, mobile, roleIds, deptIds=None):
    # role: 0=企业管理员 3=部门管理员 5=超级管理员 6=薪资管理员 7=考勤管理员 8=资费管理员
    deptIdLi = []
    if roleIds == 0 :
        deptIdLi = [0]
    elif roleIds == 3 or roleIds > 5:
        deptIdLi = deptIds
    args = {
        'url' : '/entadmin/saveAdmin',
        'data' : {
            'uid' : uid,
            'adminMobile' : mobile,
            'roleIds' : [roleIds],
            'deptIds' : deptIdLi
        }
    }
    return http_lib.http(args)

def deleteAdmin(mobile):
    args = {
        'url' : '/entadmin/deleteAdmin',
        'data' : {
            'adminMobile' : mobile,
            'roleIds' : [0],
        }
    }
    return http_lib.http(args)

def getAdminList(role):
    """
    获取管理员列表
    :param role: 0=企业管理员 3=部门管理员 5=超级管理员 6=薪资管理员 7=考勤管理员 8=资费管理员
    :return:
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/getAdminList?roleId=%s&_=%s" % (role, timestamp)
    }
    return http_lib.http(args)

if __name__ == '__main__':

    # li = [123, 124, 125, 126, 127, 128, 129, 130]
    print getAdminList(5).body

    # re = getUsers(0,1,10)
