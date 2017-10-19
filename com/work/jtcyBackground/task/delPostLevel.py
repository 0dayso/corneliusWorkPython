#! usr/bin/python
# coding:UTF-8
import sys

sys.path.append('..')
from core import apis
from core import login


def delPostLevel():
    """
    删除我的企业 - 职级
    """
    roles = apis.getPostLevel()
    print roles
    for i in roles:
        print "开始删除" + str(i) + "的职级"
        apis.delPostLevel(i)


if __name__ == '__main__':
    login.login()
    delPostLevel()