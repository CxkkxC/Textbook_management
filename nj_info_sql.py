# -*- coding:utf-8 -*-
import sqlite3
# 打开年级数据库
def nj_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists nj_info(
        id integer PRIMARY KEY autoincrement,
        nj varchar(128),
        nj_number varchar(5),
        student_sl varchar(128))""")
        return cur, conn

#查询年级全部年级
def nj_slectTable():
        hel = nj_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from nj_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往年级数据库中添加内容
def nj_insertData(nj,nj_number,student_sl):
        hel = nj_opendb()
        hel[1].execute("insert into nj_info(nj,nj_number,student_sl)values (?,?,?)",(nj,nj_number,student_sl))
        hel[1].commit()
        hel[1].close()
    
#   删除年级数据库中的全部内容
def nj_delalldb():
        hel = nj_opendb()              # 返回游标conn
        hel[1].execute("delete from nj_info")
        hel[1].commit()
        hel[1].close()
