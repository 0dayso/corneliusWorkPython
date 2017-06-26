#! usr/bin/python
# coding:UTF-8
import time

from datebase import db
from datebase2 import db_2


def findUid(phoneNum):
    sql = "SELECT uid FROM t_org_user where mobile = md5(%s)" % phoneNum
    if len(db.query(sql)) == 0:
        if len(db_2.query(sql)) == 0:
            print "t_org_user表里没有【%s】的数据"%phoneNum
            print "请把后台的手机号删除，重新加一次"
            return False
        else:
            return db_2.query(sql)[0][0]
    else:
        return db.query(sql)[0][0]

def delData(uid):

    sql = "select id,uid from shinemo_im.t_org_user where uid = '%s';"%uid

    dic = db.outputDict(sql,[id,uid])
    # print dic,dic[0][id]
    if len(dic)>0:
        sql1 = "delete from t_org_user where id='%s';"%dic[0][id]
        db.update(sql1)
    else:
        dic2 = db_2.outputDict(sql,[id,uid])
        # print dic2,dic2[0][id]
        sql1 = "delete from t_org_user where id='%s';"%dic2[0][id]
        db.update(sql1)


 
def findCheckCode(phoneNum):
    uid = findUid(phoneNum)
    if uid:
        sql = "SELECT checkcode FROM t_login_user where id = '%s'" % uid
        if len(db.query(sql)) == 0:
            if len(db_2.query(sql)) == 0:
                print "t_login_user表里没有查到uid为【%s】的数据！" % uid
                # print "程序开始更新数据库数据，请等待"
                # delData(uid)
                # print "数据已更新，请把通讯录里的人员删除后，再重新添加一次就可以了！！！"
            else:
                string = db_2.query(sql)[0][0]
                if len(string) == 0:
                    print "没有找到验证码！"
                else:
                    print "验证码为： ",  string
        else:
            string1 = db.query(sql)[0][0]
            if len(string1) == 0:
                print "没有找到验证码！"
            else:
                print "验证码为： ",  string1

def findOpenRegisterCheckCode(phoneNum):
    sql = "SELECT checkcode FROM t_mobile_checkcode WHERE mobile = %s" % phoneNum
    if len(db.query(sql)) == 0:
        if len(db_2.query(sql)) == 0:
            print "t_mobile_checkcode表里没有【%s】的验证码"%phoneNum
        else:
            s = db_2.query(sql)[0][0]
            if len(s)==0:
                print "验证码为空"
            else:
                print "验证码为： ", s
    else:
        s = db.query(sql)[0][0]
        if len(s)==0:
            print "验证码为空"
        else:
            print "验证码为： ", s

def rFindCheckCode():
    print "**************************************************************************************"
    print "******注意：手机号如果输入错误，会退出程序，程序没有做相应的处理，请重启再次输入******"
    print "**************************************************************************************"
    repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):").replace(" ", "")
    if len(repeat) == 11:
        while len(repeat) == 11:
            # repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):")
            if len(repeat)==11:
                findCheckCode(repeat)
                print "=================================================="
                repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):").replace(" ", "")
                if repeat == "1" or repeat == "2" or repeat == "3" or repeat == "4":
                    print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
                    return repeat
    elif repeat == "1" or repeat == "2" or repeat == "3" or repeat == "4":
        print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
        return repeat
    else:
        print "程序没有找到要执行的命令，退出程序"

    # else:
    #     # phoneNum2 = raw_input("请输入要查询的验证码的手机号(输入手机号不正确就会退出程序):")
    #     # if len(phoneNum2)==11:
    #     #     print "验证码为： ", findCheckCode(phoneNum2)
    #     #     for i in range(10):
    #     #         time.sleep(1)
    #     #         print str(10-i)+"后关闭程序"
    #     return raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):")



def findUid1(phoneNum):
    sql = "SELECT uid FROM t_org_user where mobile = md5(%s)" % phoneNum
    if len(db.query(sql)) == 0:
        if len(db_2.query(sql)) == 0:
            print "t_org_user表里没有【%s】的数据"%phoneNum
            pass
        else:
            return db_2.query(sql)[0][0]
            # print db_2.query(sql)[0][0]
    else:
        return db.query(sql)[0][0]
        # print db.query(sql)[0][0]

""" 通过uid查找到姓名 """
def findName(uid):
    sql = "SELECT name FROM t_org_user where uid = %s" % uid
    if len(db.query(sql)) == 0:
        if len(db_2.query(sql)) == 0:
            print "t_org_user表里没有【%s】的数据"%uid
            pass
        else:
            return db_2.query(sql)[0][0]
    else:
        return db.query(sql)[0][0]

""" 通过uid查找到公司 """
def findOrgId(uid):
    sql = "SELECT org_id FROM t_org_uid where uid = %s" % uid
    if len(db.query(sql)) == 0:
        if len(db_2.query(sql)) == 0:
            print "t_org_uid表里没有【%s】的数据"%uid
            pass
        else:
            return db_2.query(sql)
    else:
        return db.query(sql)


""" 通过手机号查找UID """
def viaMobileFindUid():
    phoneNum = raw_input("请输入要查询uid的手机号: ").replace(" ", "")
    if len(phoneNum)==11:
        while len(phoneNum)==11:
            print "uid = ", findUid1(phoneNum)
            phoneNum = raw_input("请输入要查询uid的手机号: ").replace(" ", "")
        if phoneNum == "1" or phoneNum == "2" or phoneNum == "3":
                print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
                return phoneNum
    elif phoneNum == "1" or phoneNum == "2" or phoneNum == "3":
        print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
        return phoneNum


""" 通过uid查找orgID和其中一个的名字 """
def viaUidFindOrgIdAndName():
    uid1 = raw_input("请输入uid: ").replace(" ", "")
    if len(uid1) > 2:
        while len(uid1) > 2:
            name = findName(uid1)
            orgIdList = findOrgId(uid1)
            print '姓名： ', name, '所属公司： ', orgIdList
            uid1 = raw_input("请输入uid: ").replace(" ", "")
            if uid1 == "1" or uid1 == "2" or uid1 == "3":
                print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
                return uid1
    elif uid1 == "1" or uid1 == "2" or uid1 == "3":
        print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
        return uid1

""" 查找开放注册的验证码 """
def rFindOpenRegisterCheckCode():
    repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):").replace(" ", "")
    if len(repeat) == 11:
        while len(repeat) == 11:
            # repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):")
            if len(repeat)==11:
                findOpenRegisterCheckCode(repeat)
                print "=================================================="
                repeat = raw_input("请输入要查询的验证码的手机号(输入任意不等于11位的内容就会退出程序):").replace(" ", "")
                if repeat == "1" or repeat == "2" or repeat == "3" or repeat == "4":
                    print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
                    return repeat
    elif repeat == "1" or repeat == "2" or repeat == "3" or repeat == "4":
        print "1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出"
        return repeat
    else:
        print "程序没有找到要执行的命令，退出程序"





if __name__ == '__main__':
    # uid = "101010011397329"
    # print findName(uid)
    # print findOrgId(uid)

    case = raw_input("1:查找验证码； 2:手机号找uid; 3:uid查所属企业；4:查找开放注册验证码；5及其以上退出")
    while case == "1" or case == "2" or case == "3" or case == "4":
        if case == "1":
            print "\n进入查找验证："
            case = rFindCheckCode()
        if case == "2":
            print "\n进入查找uid："
            case = viaMobileFindUid()
        if case == "3":
            print "\n进入查找uid查企业："
            case = viaUidFindOrgIdAndName()
        if case == "4":
            print "\n进入查找开放注册验证码："
            case = rFindOpenRegisterCheckCode()
        if case != "1" and case != "2" and case != "3" and case != "4":
            print "退出程序了"
            break



