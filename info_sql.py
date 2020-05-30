# -*- coding:utf-8 -*-
import sqlite3
# 打开信息数据库
def all_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists all_info(
        id integer PRIMARY KEY autoincrement,
        datetime varchar(128),
        info varchar(128))""")
        return cur, conn
    
# #查询所有列名
# def all_lie_info():
#     hel = all_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from all_info")
#     col_info_list = [tuple[0] for tuple in cur.description]  
#     return col_info_list
#     cur.close()

#查询信息全部信息
def all_slectTable():
        hel = all_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from all_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往信息数据库中添加内容
def all_insertData(datetime,info):
        hel = all_opendb()
        hel[1].execute("insert into all_info(datetime,info)values (?,?)",(datetime,info))
        hel[1].commit()
        hel[1].close()
    
#   删除信息数据库中的全部内容
def all_delalldb():
        hel = all_opendb()              # 返回游标conn
        hel[1].execute("delete from all_info")
        hel[1].commit()
        hel[1].close()
