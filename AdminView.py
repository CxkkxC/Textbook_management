# -*- coding:utf-8 -*-
from tkinter import * 
from tkinter.messagebox import * 
from tkinter import ttk
import time
#出入库信息
from info_sql import *
#教材订购
from jcdg_info_sql import *
#教材入库
from jcrk_info_sql import *
#教材领取
from jclq_info_sql import *
#学生信息
from student_info_sql import *
#课程信息
from subject_info_sql import *
#年级信息
from nj_info_sql import *



class BookFrame(Frame): # 继承Frame类 
    def __init__(self, master=None):
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root
        self.createPage() 

    def createPage(self):
        Button(self,text="年级管理",command=self.nj_admin,width=50,height=5).pack(pady=10,ipady=8)
        Button(self,text="课程管理",command=self.subject_admin,width=50,height=5).pack(pady=10,ipady=8)
        Button(self,text="学生管理",command=self.student_admin,width=50,height=5).pack(pady=10,ipady=8)
        
    def student_admin(self):
        def info():
            self.see_info = Toplevel(self.root)
            self.see_info.title('学生信息')
            b=['序号','学号','姓名','年龄','性别','是否交学费']
            tree = ttk.Treeview(self.see_info,columns=b,show='headings')
            tree.column('0',width=50,anchor='center')
            tree.heading('0',text=b[0])
            for i in range(1,len(b)):
                tree.column(str(i),width=100,anchor='center')
                tree.heading(str(i),text=b[i])
            #获得课程全部信息
            a=user_slectTable()
            for i in a:
                tree.insert('','end',values=list(i))
            tree.grid()
            
        def add():
            def insert_sql():
                '''
                添加学生
                1:获取学生姓名，年龄，学号，性别
                2:将获取到的账号与数据库文件配对，查看是否存在相同学号，如不存在，将学生插入数据库文件，存在则提示修改账户名
                异常捕获：信息未填写
                '''
                try:
                    age = self.new_age.get()
                    number = self.new_number.get()
                    name = self.new_name.get()
                    sex = self.student_sex.get()
                    flag='已交'
                    "入学年份  大几  班级  序号"
                    "2017 1 01 01"
                    if len(number) < 9:
                        showinfo(title='提示', message='学号为9位的数字，请重新输入！')
                    else:
                        STU=user_showdb(number)#先判断账号是否存在于学生或者教师数据库
                        if STU == None:
                            user_insertData(number,name,age,sex,flag)
                            showinfo(title='提示', message='注册成功')
                            self.window_sign_up.destroy()
                        else:
                            self.window_sign_up.destroy()
                            showinfo(title='提示',message='学号重复，注册失败，请修改学号！')  
                except:
                    showinfo(title='错误',message='未知错误，请重新输入！')
                
            self.window_sign_up = Toplevel(self.root)
            winWidth = 300
            winHeight = 250
            self.window_sign_up.title('注册窗口')
            screenWidth = self.window_sign_up.winfo_screenwidth()
            screenHeight = self.window_sign_up.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.window_sign_up.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.window_sign_up.resizable(0, 0)


            self.new_name = StringVar()
            Label(self.window_sign_up, text='姓名: ').place(x=10, y=10) 
            entry_new_name = Entry(self.window_sign_up, textvariable=self.new_name) 
            entry_new_name.place(x=130, y=10)

            self.new_age= StringVar()
            Label(self.window_sign_up, text='年龄: ').place(x=10, y=50)
            entry_usr_age = Entry(self.window_sign_up, textvariable=self.new_age)
            entry_usr_age.place(x=130, y=50)

            self.new_number = StringVar()
            Label(self.window_sign_up, text='学号: ').place(x=10, y=90)
            entry_student_number = Entry(self.window_sign_up, textvariable=self.new_number)
            entry_student_number.place(x=130, y=90)


            self.student_sex = StringVar()
            Label(self.window_sign_up, text='性别: ').place(x=10, y=130)
            entry_student_sex = Entry(self.window_sign_up, textvariable=self.student_sex)
            entry_student_sex.place(x=130, y=130)

            sign_up = Button(self.window_sign_up, text='注册',width=10,height=2,command=insert_sql)
            sign_up.place(x=180, y=180)
        
        self.student_info = Toplevel(self.root)
        winWidth = 300
        winHeight = 300
        self.student_info.title('学生窗口')
        screenWidth = self.student_info.winfo_screenwidth()
        screenHeight = self.student_info.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.student_info.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.student_info.resizable(0, 0)
        
        Button(self.student_info,text="学生添加",command=add,width=50,height=5).pack(pady=10,ipady=8)
        Button(self.student_info,text="学生信息",command=info,width=50,height=5).pack(pady=10,ipady=8)
    
    def nj_admin(self):
        #获取年级信息
        a=nj_slectTable()
        strs=''
        for i in a:
            strs+='\n年级名称：'+i[1]+'\n年级编号：'+i[2]+'\n学生数量：'+i[3]+"人\n"
        showinfo(title='年级信息',message=strs[1::])
    
    def subject_admin(self):
        #添加课程
        def add_subject():
            #确认添加
            def sure_add():
                try:
                    #获取课程号
                    number=self.subject_number.get()
                    #获取课程名
                    name=self.subject_name.get()
                    subject_insertData(number,name)
                    showinfo(title='信息',message='课程添加成功')
                    self.add.destroy()
                except:
                    showinfo(title='信息',message='课程添加失败')

            self.add = Toplevel(self.root)
            winWidth = 250
            winHeight = 130
            self.add.title('课程窗口')
            screenWidth = self.add.winfo_screenwidth()
            screenHeight = self.add.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.add.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.add.resizable(0, 0)
            
            #输入的变量
            self.subject_number = StringVar()
            #标签
            Label(self.add, text='课程号: ').place(x=25, y=10)
            #输入框
            Entry(self.add, textvariable=self.subject_number).place(x=75, y=10)
            
            self.subject_name= StringVar()
            Label(self.add, text='课程名: ').place(x=25, y=50)
            Entry(self.add, textvariable=self.subject_name).place(x=75, y=50)
            
            Button(self.add,text="确认添加",command=sure_add).place(x=130, y=90)
            
        #查看课程信息    
        def see_subject():
            self.see_info = Toplevel(self.root)
            self.see_info.title('课程信息')
            b=['序号','课程号','课程名']
            tree = ttk.Treeview(self.see_info,columns=b,show='headings')
            tree.column('0',width=50,anchor='center')
            tree.heading('0',text=b[0])
            for i in range(1,len(b)):
                tree.column(str(i),width=100,anchor='center')
                tree.heading(str(i),text=b[i])
            #获得课程全部信息
            a=subject_slectTable()
            for i in a:
                tree.insert('','end',values=list(i))
            tree.grid()
            
        def alter_subject():
            def sure_alter():
                try:
                    #获取课程号
                    number=self.subject_number.get()
                    #获取课程名
                    name=self.subject_name.get()
                    subject_alter(number,name)
                    showinfo(title='信息',message='课程修改成功')
#                     self.alter.destroy()
                except:
                    showinfo(title='信息',message='没有该课程号')
                    
            #打开课程信息查看课程号修改课程名        
            see_subject()
            self.alter = Toplevel(self.root)
            winWidth = 250
            winHeight = 150
            self.alter.title('课程窗口')
            screenWidth = self.alter.winfo_screenwidth()
            screenHeight = self.alter.winfo_screenheight()
            x = int((screenWidth - winWidth) / 2)
            y = int((screenHeight - winHeight) / 2)
            # 设置窗口初始位置在屏幕居中
            self.alter.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
            # 设置窗口图标
            # root.iconbitmap("./image/icon.ico")
            # 设置窗口宽高固定
            self.alter.resizable(0, 0)
            
            #输入的变量
            self.subject_number = StringVar()
            #标签
            Label(self.alter, text='课程号: ').place(x=25, y=10)
            #输入框
            Entry(self.alter, textvariable=self.subject_number).place(x=75, y=10)
            
            self.subject_name= StringVar()
            Label(self.alter, text='课程名: ').place(x=25, y=50)
            Entry(self.alter, textvariable=self.subject_name).place(x=75, y=50)
            
            Button(self.alter,text="确认修改",command=sure_alter).place(x=130, y=90)
            
        self.subject_info = Toplevel(self.root)
        winWidth = 300
        winHeight = 400
        self.subject_info.title('课程窗口')
        screenWidth = self.subject_info.winfo_screenwidth()
        screenHeight = self.subject_info.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.subject_info.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.subject_info.resizable(0, 0)
        
        Button(self.subject_info,text="课程添加",command=add_subject,width=50,height=5).pack(pady=10,ipady=8)
        Button(self.subject_info,text="课程信息",command=see_subject,width=50,height=5).pack(pady=10,ipady=8)
        Button(self.subject_info,text="课程修改",command=alter_subject,width=50,height=5).pack(pady=10,ipady=8)
#         Button(self.subject_info,text="课程删除",command='#',width=50,height=5).pack(pady=10,ipady=8)
        
class TakeFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.createPage() 
    
    def ls(self):
        global numbers
        def treeviewClick(event):
            for item in tree.selection():
                item_text=tree.item(item,"values")
                book_select=list(item_text)
                #是否订购提示框
                a=askokcancel(title='提示', message='是否领取该教材？')
                #如果确认的话
                if a:
                    datetimes=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    info="学号为：%s 的学生领取教材，教材名：%s，单价：%s"%(numbers,book_select[2],str(float(book_select[4])/float(book_select[3])))
                    all_insertData(datetimes,info)
                    showinfo(title='提示',message='领取成功！')
#                     self.rk_info.destroy()
                #否则什么都不做
                else:
                    pass
        self.rk_info = Toplevel(self.root)
        self.rk_info.title('教材信息')
        b=['序号',"书号","教材名称","数量","总价"]
        tree = ttk.Treeview(self.rk_info,columns=b,show='headings')
        tree.column('0',width=50,anchor='center')
        tree.heading('0',text=b[0])
        for i in range(1,len(b)):
            tree.column(str(i),width=150,anchor='center')
            tree.heading(str(i),text=b[i])
        #获得教材全部信息
        a=jcrk_slectTable()
        for i in a:
            tree.insert('','end',values=list(i))
        tree.grid()
        tree.bind("<ButtonRelease-1>",treeviewClick)
        
    def get_number(self):
        def sure_dg():
            global numbers
            numbers=str(self.number.get())
            STU=user_showdb(numbers)#先判断账号是否存在于学生或者教师数据库
            if STU == None:
                showinfo(title='错误',message='数据库没有该学号学生信息，请重新输入！')
                self.jc_dg.destroy()
            else:
                self.jc_dg.destroy()
                self.ls()
            
        self.jc_dg = Toplevel(self.root)
        winWidth = 250
        winHeight = 130
        self.jc_dg.title('获取学号')
        screenWidth = self.jc_dg.winfo_screenwidth()
        screenHeight = self.jc_dg.winfo_screenheight()
        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.jc_dg.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
        self.jc_dg.resizable(0, 0)

        #输入的变量
        self.number = StringVar()
        #标签
        Label(self.jc_dg, text='输入学号: ').place(x=25, y=10)
        #输入框
        Entry(self.jc_dg, textvariable=self.number).place(x=75, y=10)

        Button(self.jc_dg,text="确认",command=sure_dg).place(x=130, y=90)

    def createPage(self):
        Button(self,text="学生领书",command=self.get_number,width=50,height=5).pack(pady=10,ipady=8)
    
class TextbookFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root
        self.createPage() 

    def dg(self):
        book_select=[]
        def treeviewClick(event):
            def sure_dg():
                try:
                    number=self.jc_number.get()
                    all_money=str(float(number)*float(book_select[6]))
                    jcrk_insertData(book_select[5],book_select[1],str(number),all_money)
                    datetimes=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
                    info="订购教材：教材名：%s，单价：%s，数量：%s，总价：%s"%(book_select[1],book_select[6],str(number),str(float(number)*float(book_select[6])))
                    all_insertData(datetimes,info)
                    showinfo(title='提示',message='订购成功！')
                    self.jc_dg.destroy()
                except:
                    showinfo(title='错误',message='请输入数字！')
                    
            for item in tree.selection():
                item_text=tree.item(item,"values")
                book_select=list(item_text)
                #是否订购提示框
                a=askokcancel(title='提示', message='是否订购该教材？')
                #如果确认的话
                if a:
                    self.jc_dg = Toplevel(self.root)
                    winWidth = 250
                    winHeight = 130
                    self.jc_dg.title('订购窗口')
                    screenWidth = self.jc_dg.winfo_screenwidth()
                    screenHeight = self.jc_dg.winfo_screenheight()
                    x = int((screenWidth - winWidth) / 2)
                    y = int((screenHeight - winHeight) / 2)
                    # 设置窗口初始位置在屏幕居中
                    self.jc_dg.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x-50, y-50))
                    # 设置窗口图标
                    # root.iconbitmap("./image/icon.ico")
                    # 设置窗口宽高固定
                    self.jc_dg.resizable(0, 0)

                    #输入的变量
                    self.jc_number = IntVar()
                    #标签
                    Label(self.jc_dg, text='订购数量: ').place(x=25, y=10)
                    #输入框
                    Entry(self.jc_dg, textvariable=self.jc_number).place(x=75, y=10)

                    Button(self.jc_dg,text="确认订购",command=sure_dg).place(x=130, y=90)
                #否则什么都不做
                else:
                    pass
        self.jc_info = Toplevel(self.root)
        self.jc_info.title('教材信息')
        b=['序号',"教材名称","出版社","作者","版次","书号","单价"]
        tree = ttk.Treeview(self.jc_info,columns=b,show='headings')
        tree.column('0',width=50,anchor='center')
        tree.heading('0',text=b[0])
        for i in range(1,len(b)):
            tree.column(str(i),width=150,anchor='center')
            tree.heading(str(i),text=b[i])
        #获得教材全部信息
        a=jcdg_slectTable()
        for i in a:
            tree.insert('','end',values=list(i))
        tree.grid()
        tree.bind("<ButtonRelease-1>",treeviewClick)
        
        #查看库存
    def rk(self):
        self.rk_info = Toplevel(self.root)
        self.rk_info.title('教材信息')
        b=['序号',"书号","教材名称","数量","总价"]
        tree = ttk.Treeview(self.rk_info,columns=b,show='headings')
        tree.column('0',width=50,anchor='center')
        tree.heading('0',text=b[0])
        for i in range(1,len(b)):
            tree.column(str(i),width=150,anchor='center')
            tree.heading(str(i),text=b[i])
        #获得教材全部信息
        a=jcrk_slectTable()
        for i in a:
            tree.insert('','end',values=list(i))
        tree.grid()
        
    def cx(self):
        self.cx_info = Toplevel(self.root)
        self.cx_info.title('教材信息')
        b=['序号',"时间","操作信息"]
        tree = ttk.Treeview(self.cx_info,columns=b,show='headings')
        tree.column('0',width=50,anchor='center')
        tree.heading('0',text=b[0])
        for i in range(1,len(b)):
            if i==2:
                tree.column(str(i),width=500,anchor='center')
                tree.heading(str(i),text=b[i])
            else:
                tree.column(str(i),width=150,anchor='center')
                tree.heading(str(i),text=b[i])
        #获得教材全部信息
        a=all_slectTable()
        for i in a:
            tree.insert('','end',values=list(i))
        tree.grid()
            
    def createPage(self):
        Button(self,text="教材订购",command=self.dg,width=50,height=5).pack(pady=10,ipady=8)
        Button(self,text="教材入库",command=self.rk,width=50,height=5).pack(pady=10,ipady=8)
        Button(self,text="教材查询",command=self.cx,width=50,height=5).pack(pady=10,ipady=8)

class aboutFrame(Frame): # 继承Frame类 
    def __init__(self, master=None): 
        Frame.__init__(self, master) 
        self.root = master #定义内部变量root 
        self.createPage() 

    def createPage(self): 
        Label(self, fg='blue',text='课程管理模块\n主要是对课程信息进行添加、查看、修改、删除等，如：课程号、课程名\n学生管理模块\n主要是对学生信息的添加、查看、修改和删除，如：学号、姓名、性别、交费情况等。\n教材选定模块\n主要是对教材选定信息进行添加、查看、修改、删除，如：选定编号、教材代码\n教材订购模块\n主要是对选定的教材进行订购，并且可以查看订单情况。\n入库登记模块\n主要是对入库信息进行添加、查看、修改、删除，如：教材代码、数量、入库价格\n学生领取模块\n主要是对学生领取教材情况进行添加、查看、修改、删除，如：学号、教材代码\n查询模块\n可以通过教材订购信息或者教材入库、出库信息进行查询。').pack() 

