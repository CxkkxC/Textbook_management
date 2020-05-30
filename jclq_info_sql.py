# -*- coding:utf-8 -*-
import sqlite3
# 打开教材领取数据库
def jclq_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists jclq_info(
        id integer PRIMARY KEY autoincrement,
        student_number varchar(12),
        jclq_name varchar(10))""")
        return cur, conn
    
# #查询所有列名
# def jclq_lie_name():
#     hel = jclq_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from jclq_info")
#     col_name_list = [tuple[0] for tuple in cur.description]  
#     return col_name_list
#     cur.close()

#查询教材领取全部信息
def jclq_slectTable():
        hel = jclq_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jclq_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往教材领取数据库中添加内容
def jclq_insertData(student_number,name):
        hel = jclq_opendb()
        hel[1].execute("insert into jclq_info(student_number,jclq_name)values (?,?)",(student_number,name))
        hel[1].commit()
        hel[1].close()
        
#查询教材领取信息
def jclq_showdb(number):
        hel = jclq_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jclq_info where student_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除教材领取数据库中的全部内容
def jclq_delalldb():
        hel = jclq_opendb()              # 返回游标conn
        hel[1].execute("delete from jclq_info")
        hel[1].commit()
        hel[1].close()
        
#   删除教材领取数据库中的指定内容
def jclq_deldb(number):
        hel = jclq_opendb()              # 返回游标conn
        hel[1].execute("delete from jclq_info where student_number="+number)
        print("已删除教材领取号为 %s 教材领取" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改教材领取数据库的内容
def jclq_alter(number,name):
        hel = jclq_opendb()
        hel[1].execute("update jclq_info set jclq_name=? where student_number="+number,(name))
        hel[1].commit()
        hel[1].close()
