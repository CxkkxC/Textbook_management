# -*- coding:utf-8 -*-
import sqlite3
# 打开学生数据库
def user_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists student_info(
        id integer PRIMARY KEY autoincrement,
        student_number varchar(12),
        student_name varchar(10),
        student_age varchar(2),
        student_sex varchar(10),
        student_flag varchar(12))""")
        return cur, conn
    
# #查询所有列名
# def user_lie_name():
#     hel = user_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from student_info")
#     col_name_list = [tuple[0] for tuple in cur.description]  
#     return col_name_list
#     cur.close()

#查询学生全部信息
def user_slectTable():
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from student_info")
        res = cur.fetchall()
        return res
        cur.close()
#  往学生数据库中添加内容
def user_insertData(number,name,age,student_sex,student_flag):
        hel = user_opendb()
        hel[1].execute("insert into student_info(student_number,student_name,student_age,student_sex,student_flag)values (?,?,?,?,?)",(number,name,age,student_sex,student_flag))
        hel[1].commit()
        hel[1].close()
        
#查询学生个人信息
def user_showdb(number):
        hel = user_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from student_info where student_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除学生数据库中的全部内容
def user_delalldb():
        achievement_delalldb()
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from student_info")
        hel[1].commit()
        hel[1].close()
        
#   删除学生数据库中的指定内容
def user_deldb(number):
        hel = user_opendb()              # 返回游标conn
        hel[1].execute("delete from student_info where student_number="+number)
        print("已删除学号为 %s 学生" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改学生数据库的内容
def user_alter(number,name,pw,age):
        hel = user_opendb()
        hel[1].execute("update student_info set student_name=?, student_passworld= ?,age=? where student_number="+number,(name,pw,age))
        hel[1].commit()
        hel[1].close()
