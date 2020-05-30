# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from student_info_sql import * 
from AdminView import *
from tkinter import ttk

class AdminPage(object):
    def __init__(self, master=None): 
        self.root = master #定义内部变量root 
        self.root.geometry('%dx%d' % (650, 400)) #设置窗口大小 
        self.root.resizable(0,0) #防止用户调整尺寸
        self.createPage() 

    def createPage(self): 
        self.admin_menuPage = admin_MenuFrame(self.root) # 创建不同Frame 

class admin_MenuFrame(Frame): # 继承Frame类 
    def __init__(self, master=None):
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root
        self.createPage()

    def createPage(self):
        #书籍需求信息管理页面
        self.bookPage = BookFrame(self.root) # 创建不同Frame 
        #领书信息读入页面
        self.takePage = TakeFrame(self.root)
        #教材管理页面
        self.textbookPage = TextbookFrame(self.root)
        #软件关于页面
        self.aboutPage = aboutFrame(self.root)
        
        #书籍需求信息管理页面
        self.bookPage.pack() #默认显示界面 
        
        menubar = Menu(self.root) 
        menubar.add_command(label='书籍需求信息管理', command = self.bookData)
        menubar.add_command(label='领书信息读入', command = self.takeData)
        menubar.add_command(label='教材管理', command = self.textbookData)
        menubar.add_command(label='软件使用帮助', command = self.aboutData)
        self.root['menu'] = menubar # 设置菜单栏 

    def bookData(self): 
        self.bookPage.pack()
        self.textbookPage.pack_forget()
        self.takePage.pack_forget()
        self.aboutPage.pack_forget()


    def takeData(self): 
        self.bookPage.pack_forget()
        self.textbookPage.pack()
        self.takePage.pack_forget()
        self.aboutPage.pack_forget()


    def textbookData(self): 
        self.bookPage.pack_forget()
        self.textbookPage.pack_forget()
        self.takePage.pack()
        self.aboutPage.pack_forget()

    def aboutData(self): 
        self.bookPage.pack_forget()
        self.textbookPage.pack_forget()
        self.takePage.pack_forget()
        self.aboutPage.pack()

    
        
#  def see_student_info(self):
#     self.see_students = Toplevel(self.root)
#     self.see_students.title('学生信息')
#     b=['序号','学号','姓名','密码','年龄','班级','性别','身份证','手机号','民族','是否在读']
#     tree = ttk.Treeview(self.see_students,columns=b,show='headings')
#     tree.column('0',width=50,anchor='center')
#     tree.heading('0',text=b[0])
#     for i in range(1,len(b)):
#         if i==7:
#             tree.column(str(i),width=150,anchor='center')
#             tree.heading(str(i),text=b[i])
#         else:
#             tree.column(str(i),width=100,anchor='center')
#             tree.heading(str(i),text=b[i])

#     a=user_slectTable()
#     for i in a:
#         tree.insert('','end',values=list(i))
#     tree.grid()