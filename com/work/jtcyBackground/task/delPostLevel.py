#! usr/bin/python
# coding:UTF-8
import sys
sys.path.append('..')
from core import apis


def delPostLevel():
    """
    删除我的企业 - 职级
    """
    roles = apis.getPostLevel()
    print roles
    for i in roles:
        apis.delPostLevel(i)


if __name__ == '__main__':
    delPostLevel()