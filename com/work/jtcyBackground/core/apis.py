#! usr/bin/python
# coding:UTF-8
import time
import sys
sys.path.append('..')
from core import http_lib
from basic import config_file

class Response():
    pass

def getDepartments(parentId):
    """
    获取部门下的部门列表
    :param parentId:父部门ID
    :return:
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept?parentId=%s&_=%s" % (parentId, timestamp)
    }
    return http_lib.http(args)

def getAllDepartmentsId(parentId, li):
    """
    获取parentId部门下的所有部门及其所有子部门的部门id
    :param parentId:
    :return:[1, 5, 6, 2, 7, 8, 10, 12, 11, 13, 9, 3, 4]
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept?parentId=%s&_=%s" % (parentId, timestamp)
    }
    result = http_lib.http(args).jBody
    for dept in result['data']['deptList']:
        deptId = dept['id']
        li.append(deptId)
        getAllDepartmentsId(deptId, li)
    return li

def deleteDeptAndUser(parentId, pageIndex, pageSize):
    """
    删除parentId下面的所有的人员和本部门
    :param parentId:
    :return:
    """
    if parentId != 0:
        li = getAllDepartmentsId(parentId, [parentId])
    else:
        li = getAllDepartmentsId(parentId, [])
    print li

    for deptId in li:
        userId = getUsersKey(deptId, pageIndex, pageSize)
        deptIds = getAllDepartmentsId(deptId, [])
        if len(deptIds) > 0:
            for deptId1 in deptIds:
                deleteDeptAndUser(deptId1, pageIndex, pageSize)
        else:
            if len(userId) != 0:
                strUserId = ",".join(userId)
                deleteUser(strUserId)
                deleteDept(deptId)
            else:
                deleteDept(deptId)

def test(parentId, pageIndex, pageSize):
    userId = getUsersKey(parentId, pageIndex, pageSize)
    if len(userId) != 0:
        strUserId = ",".join(userId)
        deleteUser(strUserId)
    deptIds = getAllDepartmentsId(parentId, [])
    if len(deptIds) > 0:
        for deptId1 in deptIds:
            test(deptId1, pageIndex, pageSize)
    else:
        print "删除部门id=" + str(parentId) + "的部门"
        deleteDept(parentId)






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

def getUsersKey(deptId, pageIndex, pageSize):
    """
    获取人员列表
    :param deptId: 要获取部门人员的部门ID
    :param pageIndex: 从第几页开始
    :param pageSize: 每页多少人
    :return: keyList
    """
    timestamp = str(int(time.time() * 1000))
    args = {
        'url': "http://admin.jituancaiyun.net/entadmin/contact/dept/users?deptId=%s&pageIndex=%s&pageSize=%s&_=%s" % (
            deptId, pageIndex, pageSize, timestamp)
    }
    result = http_lib.http(args).jBody
    li = []
    if None != result['data']['users']:
        for user in result['data']['users']:
            li.append(str(user['id']))
    return li

def deleteUser(strUserId):
    """
    删除人员
    """
    args = {
        'url' : '/entadmin/batchDelUser',
        'data' : {
            'userIds' : strUserId # 参数样式：'128','129','130','131','132'
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

    if config_file.IS_ON_LINE:
        args = {
            'url': "https://admin.jituancaiyun.com/entadmin/getAdminList?roleId=%s&_=%s" % (role, timestamp)
        }
    else:
        args = {
            'url': "http://admin.jituancaiyun.net/entadmin/getAdminList?roleId=%s&_=%s" % (role, timestamp)
        }
    resp = http_lib.http(args).jBody
    d = Response()
    uids = []
    adminIds = []
    mobiles = []
    for i in resp['data']:
        uids.append(i['uid'])
        adminIds.append(i['adminId'])
        mobiles.append(i['adminMobile'])
    d.uid = uids
    d.adminId = adminIds
    d.mobile = mobiles
    return d


def getOrgRole():
    """
    获取 功能角色 - 管理员角色
    :return: data data.id 返回所有的角色 data.name返回所有的角色名称
    """
    timestamp = str(int(time.time() * 1000))

    if config_file.IS_ON_LINE:
        args = {
            'url': "https://admin.jituancaiyun.com/entadmin/getOrgRole?_=%s" % timestamp
        }
    else:
        args = {
            'url': "http://admin.jituancaiyun.net/entadmin/getOrgRole?_=%s" % timestamp
        }
    resp = http_lib.http(args)
    body = resp.jBody
    d = Response()
    ids = []
    names = []
    for i in body['data']:
        ids.append(i['id'])
        names.append(i['name'])
    d.id = ids
    d.name = names
    return d

def deleteRole(roleId):
    """
    删除 功能角色 - 管理员角色
    :param roleId: 角色Id
    :return:
    """

    timestamp = str(int(time.time() * 1000))

    if config_file.IS_ON_LINE:
        args = {
            'url': "https://admin.jituancaiyun.com/entadmin/deleteRole?roleId=%s&_=%s" % (roleId, timestamp)
        }
    else:
        args = {
            'url': "http://admin.jituancaiyun.net/entadmin/deleteRole?roleId=%s&_=%s" % (roleId, timestamp)
        }
    http_lib.http(args)



if __name__ == '__main__':
    # li = [123, 124, 125, 126, 127, 128, 129, 130]
    # print getOrgRole()
    d = getAdminList(0)
    print d.uid
    print d.adminId
    print d.mobile
    # print getUsersKey(1,1,100)
    # print getAllDepartmentsId(0,[])

    # re = getUsers(0,1,10)
