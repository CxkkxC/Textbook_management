# -*- coding:utf-8 -*-
import sqlite3
# 打开教材入库数据库
def jcrk_opendb():
        conn = sqlite3.connect("jc_admin.db")
        cur = conn.execute("""create table if not exists jcrk_info(
        id integer PRIMARY KEY autoincrement,
        jcrk_number varchar(12),
        jcrk_name varchar(10),
        jcrk_sl varchar(10),
        jcrk_price varchar(5))""")
        return cur, conn
    
# #查询所有列名
# def jcrk_lie_name():
#     hel = jcrk_opendb()
#     cur = hel[1].cursor()
#     cur.execute("select * from jcrk_info")
#     col_name_list = [tuple[0] for tuple in cur.description]  
#     return col_name_list
#     cur.close()

#查询教材入库全部信息
def jcrk_slectTable():
        hel = jcrk_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jcrk_info")
        res = cur.fetchall()
        return res
        cur.close()
        
#  往教材入库数据库中添加内容
def jcrk_insertData(number,name,jcrk_sl,jcrk_price):
        hel = jcrk_opendb()
        hel[1].execute("insert into jcrk_info(jcrk_number,jcrk_name,jcrk_sl,jcrk_price)values (?,?,?,?)",(number,name,jcrk_sl,jcrk_price))
        hel[1].commit()
        hel[1].close()
        
#查询教材入库信息
def jcrk_showdb(number):
        hel = jcrk_opendb()
        cur = hel[1].cursor()
        cur.execute("select * from jcrk_info where jcrk_number="+number)
        res = cur.fetchone()
        cur.close()
        return res
    
#   删除教材入库数据库中的全部内容
def jcrk_delalldb():
        hel = jcrk_opendb()              # 返回游标conn
        hel[1].execute("delete from jcrk_info")
        hel[1].commit()
        hel[1].close()
        
#   删除教材入库数据库中的指定内容
def jcrk_deldb(number):
        hel = jcrk_opendb()              # 返回游标conn
        hel[1].execute("delete from jcrk_info where jcrk_number="+number)
        print("已删除教材入库号为 %s 教材入库" %number)
        hel[1].commit()
        hel[1].close()
        
#  修改教材入库数据库的内容
def jcrk_alter(number,name):
        hel = jcrk_opendb()
        hel[1].execute("update jcrk_info set jcrk_name=? where jcrk_number="+number,(name))
        hel[1].commit()
        hel[1].close()
