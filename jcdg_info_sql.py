# -*- coding:utf-8 -*-
import sqlite3
# 打开教材订购数据库
def jcdg_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists jcdg_info(
        id integer PRIMARY KEY autoincrement,
        jcdg_name varchar(128),
        jcdg_cbs varchar(128),
        jcdg_author varchar(128),
        jcdg_bc varchar(128),
        jcdg_number varchar(12),
        jcdg_price varchar(5))""")
        return cur, conn
    
# #查询所有列名
# def jcdg_lie_name():
#     hel = jcdg_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from jcdg_info")
#     col_name_list = [tuple[0] for tuple in cur.description]  
#     return col_name_list
#     cur.close()

#查询教材订购全部信息
def jcdg_slectTable():
        hel = jcdg_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jcdg_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往教材订购数据库中添加内容
def jcdg_insertData(jcdg_name,jcdg_cbs,jcdg_author,jcdg_bc,jcdg_number,jcdg_price):
        hel = jcdg_opendb()
        hel[1].execute("insert into jcdg_info(jcdg_name,jcdg_cbs,jcdg_author,jcdg_bc,jcdg_number,jcdg_price)values (?,?,?,?,?,?)",(jcdg_name,jcdg_cbs,jcdg_author,jcdg_bc,jcdg_number,jcdg_price))
        hel[1].commit()
        hel[1].close()
        
#查询教材订购信息
def jcdg_showdb(name):
        hel = jcdg_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jcdg_info where jcdg_name="+name)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除教材订购数据库中的全部内容
def jcdg_delalldb():
        achievement_delalldb()
        hel = jcdg_opendb()              # 返回游标conn
        hel[1].execute("delete from jcdg_info")
        hel[1].commit()
        hel[1].close()
        
#   删除教材订购数据库中的指定内容
def jcdg_deldb(number):
        hel = jcdg_opendb()              # 返回游标conn
        hel[1].execute("delete from jcdg_info where jcdg_number="+number)
        print("已删除教材订购号为 %s 教材订购" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改教材订购数据库的内容
def jcdg_alter(number,name):
        hel = jcdg_opendb()
        hel[1].execute("update jcdg_info set jcdg_name=? where jcdg_number="+number,(name))
        hel[1].commit()
        hel[1].close()
