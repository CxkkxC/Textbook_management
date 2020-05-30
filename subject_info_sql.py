# -*- coding:utf-8 -*-
import sqlite3
# 打开课程数据库
def subject_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists subject_info(
        id integer PRIMARY KEY autoincrement,
        subject_number varchar(12),
        subject_name varchar(10))""")
        return cur, conn
    
# #查询所有列名
# def subject_lie_name():
#     hel = subject_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from subject_info")
#     col_name_list = [tuple[0] for tuple in cur.description]  
#     return col_name_list
#     cur.close()

#查询课程全部信息
def subject_slectTable():
        hel = subject_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from subject_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往课程数据库中添加内容
def subject_insertData(number,name):
        hel = subject_opendb()
        hel[1].execute("insert into subject_info(subject_number,subject_name)values (?,?)",(number,name))
        hel[1].commit()
        hel[1].close()
        
#查询课程个人信息
def subject_showdb(number):
        hel = subject_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from subject_info where subject_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除课程数据库中的全部内容
def subject_delalldb():
        hel = subject_opendb()              # 返回游标conn
        hel[1].execute("delete from subject_info")
        hel[1].commit()
        hel[1].close()
        
#   删除课程数据库中的指定内容
def subject_deldb(number):
        hel = subject_opendb()              # 返回游标conn
        hel[1].execute("delete from subject_info where subject_number="+number)
        print("已删除课程号为 %s 课程" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改课程数据库的内容
def subject_alter(number,name):
        hel = subject_opendb()
        hel[1].execute("update subject_info set subject_name='%s' where subject_number='%s'"%(number,name))
        hel[1].commit()
        hel[1].close()
