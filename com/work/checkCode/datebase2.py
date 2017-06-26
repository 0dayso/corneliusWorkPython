# coding:UTF8

import MySQLdb as msq

class MYSQL2:
    def __init__(self):
        self.con = msq.connect(host="10.0.10.42",port=3306,user='root',passwd="shinemo123",
                               db="shinemo_im",charset='utf8')
        self.cur = self.con.cursor()

    # 关闭数据库连接
    def close(self):
        self.cur.close()
        self.con.close()

    def clean(self):
        self.close()


    # 查询数据库
    def query(self,sql):
        aa = self.cur.execute(sql)
        infos = self.cur.fetchmany(aa)
        li = []
        for info in infos:
            li.append(info)
        return li

    # 返回有多少条数据
    def count(self,sql):
        return self.cur.execute(sql)

    # 更新数据库数据
    def update(self,sql):
        # cur.execute('SET SQL_SAFE_UPDATES = 0')
        try:
            self.cur.execute(sql)
            self.con.commit()
        except:
            self.con.rollback()

    # 查询数据库，并以字典形式输入
    def outputDict(self,sql,args):

        self.cur.execute(sql)
        rows = self.cur.fetchall()

        li = []
        if len(args)!=0:
            for v in range(len(rows)):
                dic = {}
                for k in range(len(args)):
                    dic[args[k]] = rows[v][k]
                li.append(dic)
            return li
        else:
            for row in rows:
                li.append(row)
            return li

db_2 = MYSQL2()