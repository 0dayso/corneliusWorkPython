#! usr/bin/python
# coding:UTF-8
import sys
sys.path.append('..')
from core import apis


def delRoleAndAdmin():
    """
    删除功能角色和对应的管理员
    """
    roles = apis.getOrgRole().id
    print roles
    for i in roles:
        if i > 10:
            mobiles = apis.getAdminList(i).mobile
            print mobiles
            for m in mobiles:
                apis.deleteAdmin(m)
            apis.deleteRole(i)


if __name__ == '__main__':
    delRoleAndAdmin()