# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from LoginPage import * #菜单栏对应的各个子页面

# 课程管理模块
# 主要是对课程信息进行添加、查看、修改、删除等，如：课程号、课程名
# 学生管理模块
# 主要是对学生信息的添加、查看、修改和删除，如：学号、姓名、性别、交费情况等。
# 教材选定模块
# 主要是对教材选定信息进行添加、查看、修改、删除，如：选定编号、教材代码
# 教材订购模块
# 主要是对选定的教材进行订购，并且可以查看订单情况。
# 入库登记模块
# 主要是对入库信息进行添加、查看、修改、删除，如：教材代码、数量、入库价格
# 学生领取模块
# 主要是对学生领取教材情况进行添加、查看、修改、删除，如：学号、教材代码
# 查询模块
# 可以通过教材订购信息或者教材入库、出库信息进行查询。

root = Tk() #建立一个根窗口，所有窗口的基础
root.title('教材管理系统')
LoginPage(root)#进入调用登录
root.mainloop()
