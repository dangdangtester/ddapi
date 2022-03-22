# -*- coding: utf-8 -*-
# @Date    : 2021-06-02 21:54:08
# @Author  : fh
# @File    : sqlservermanage.py
import pymssql

class SqlserverOperation(object):
    conn = None

    def __init__(self, host, user, password, database, charset='utf8', port=1433):
        self.cursor = None
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset
        self.port = port

    def connect(self):
        self.conn = pymssql.connect(host=self.host, port=self.port, user=self.user, password=self.password, database=self.database,
                            charset=self.charset)
        self.cursor = self.conn.cursor(as_dict=True)

    def close(self):
        self.cursor.close()
        self.conn.close()

    def get_one(self, sql, params=()):
        result = None
        try:
            self.connect()
            self.cursor.execute(sql, params)
            result = self.cursor.fetchone()
            self.close()
        except Exception as e:
            print(e)
        return result

    def get_all(self, sql, params=()):
        list_data = ()
        try:
            self.connect()
            self.cursor.execute(sql, params)
            list_data = self.cursor.fetchall()
            self.close()
        except Exception as e:
            print(e)
        return list_data

    def insert(self, sql, params=()):
        return self.__edit(sql, params)

    def update(self, sql, params=()):
        return self.__edit(sql, params)

    def delete(self, sql, params=()):
        return self.__edit(sql, params)

    def __edit(self, sql, params):
        count = 0
        try:
            self.connect()
            count = self.cursor.execute(sql, params)
            self.conn.commit()
            self.close()
        except Exception as e:
            print(e)
        return count
'''
order_id = 1411587549
db_Order = 'Order'+str(order_id%2)
OrderBase = SqlserverOperation(host='10.255.254.194', user='writeuser', password='ddbackend', database=db_Order , charset='utf8')
#conn = pymssql.connect(host=".",user= "sa",password= "1234", database="onlinemall", charset='utf8' )
sql = 'SELECT * FROM order_amount WHERE order_id = %s'
datas = OrderBase.get_all(sql,order_id)
print(datas)
'''
