# -*- coding:utf-8 -*-
from tkinter.messagebox import * 
from tkinter import *
from tkinter import ttk
from student_info_sql import *
from AdminPage import * 

import cv2, os, math, operator
from PIL import Image
from functools import reduce
casc_path = "C:\\Users\\Cxk\\Anaconda3\Lib\site-packages\cv2\data\\haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)  #创建识别对象
def makeFace(facename):
#     cv2.namedWindow("face_recognition")
#     cv2.waitKey(0)
    cap = cv2.VideoCapture(0)  #打开摄像头
    while(cap.isOpened()):  #如果摄像头处于打开状态，则...
        try:
            ret, img = cap.read()  #读取图像
            if ret == True:#读取成功
                cv2.imshow("face_recognition", img)  #显示图像
                k = cv2.waitKey(100)  #每0.1秒读一次键盘
                if k == ord("z") or k == ord("Z"):  #如果输入z
                    cv2.imwrite(facename,img)  #把读取的img保存至facename文件
                    image = cv2.imread(facename)  #读取刚刚保存的facename文件至image变量，作为下面人脸识别函数的参数
                    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)
#                     print(faces)
                    (x, y, w, h) = (faces[0][0], faces[0][1], faces[0][2], faces[0][3])  #取出第一张人脸区域
#                     print(x,y,w,h)
                    image1 = Image.open(facename).crop((x, y, x+w, y+h))  #抓取人脸区域的图像并存至image1变量
                    image1 = image1.resize((200, 200), Image.ANTIALIAS)  #把取得的人脸区域的分辨率变为200x200
                    image1.save(facename)  #把经过处理的人脸文件保存至facename文件
                    break
        except:
            print("错误")
            continue
    cap.release()  #关闭摄像头
    cv2.destroyAllWindows()   #关闭窗口 
    return


#人脸信息比对
def cxk(number):
    diff=0.0
    recogname = "%s_recogface.jpg"%number #预存的人脸文件
    loginname = "%s_loginface.jpg"%number #登录者的人脸文件
    os.system("cls")  #清屏
    if(os.path.exists(recogname)):#如果预存的人脸文件已存在
        makeFace(loginname)  #创建登录者人脸文件
        pic1 = Image.open(recogname)  #打开预存的人脸文件
        pic2 = Image.open(loginname)  #打开登录者人脸文件
        h1 = pic1.histogram()  #取预存片文件的直方图信息
        h2 = pic2.histogram()    #取登录者图片的直方图信息
        diff = math.sqrt(reduce(operator.add, list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1)) #直方图的相似性度量
    else:  #如果预存的人脸文件不存在
        diff=200.0
    return diff

global numbers,i
i=0
class LoginPage(object):
    def __init__(self, master=None):
        self.root = master
        winWidth = 650
        winHeight = 400
        screenWidth = self.root.winfo_screenwidth()
        screenHeight = self.root.winfo_screenheight()

        x = int((screenWidth - winWidth) / 2)
        y = int((screenHeight - winHeight) / 2)
        # 设置窗口初始位置在屏幕居中
        self.root.geometry("%sx%s+%s+%s" % (winWidth, winHeight, x, y))
        # 设置窗口图标
        # root.iconbitmap("./image/icon.ico")
        # 设置窗口宽高固定
#         self.root.resizable(0, 0)
        self.number = StringVar()
        self.pw = StringVar() 
        self.createPage()
    
    def createPage(self):
        '''
        登录页面
        1:创建图片组件
        2:根目录基础上添加Frame容器
        3:Frame容器上添加注册控件
        '''
        #背景图
        bm=PhotoImage(file=r'fzkj.png')
        #背景图放置
        self.lab3=Label(self.root,image=bm)
        self.lab3.bm=bm
        self.lab3.pack()
        
        self.page = Frame(self.root) 
        self.page.pack()
        Label(self.page, text = '帐号: ').grid(row=1, column=1, pady=10,stick=W) 
        #帐号输入框
        Entry(self.page, textvariable=self.number).grid(row=1, column=2, stick=E) 
        
        Label(self.page, text = '密码: ').grid(row=2, column=1, pady=10,stick=W) 
        #密码输入框
        Entry(self.page, textvariable=self.pw, show='*').grid(row=2, column=2, stick=E) 
        
        Button(self.page, text='帐号登录', command=self.admin_loginCheck).grid(row=6, column=1,stick=W)
        Button(self.page, text='人脸登录', command=self.admin_loginChecks).grid(row=6, column=2)
        Button(self.page, text='人脸注册',command=self.signup).grid(row=6, column=3,stick=E) 
        
        self.root.bind('<KeyPress-Return>',self.admin_loginCheck)#绑定键盘上的回车登录
        
    def signup(self):
        number=self.number.get()
        recogname = "%s_recogface.jpg"%number
        if number=="":
            showinfo(title="错误",message='请输入账号！')
        elif(os.path.exists(recogname)):
            showinfo(title="错误",message='该管理已保存人脸信息，可直接登录！')
        else:
            showinfo(title="提示",message = "摄像头打开后按 z 键进行拍照!")
            makeFace(recogname)  #建立预存人脸文件
            showinfo(title='确认',message='人脸信息保存成功！')
        
    def admin_loginCheck(self,*event):
        global numbers
        '''
        管理员登录
        1:获取管理员账号与密码
        2:将获取到的账号与密码与数据库文件配对，配对成功返回值为正确，否则为错误
        3:将返回值判断，正确则登录界面清除，登录界面图片清除，进入管理员界面
        异常捕获：未填写账号或者密码
        '''
        try:
            Admin_number=self.number.get()
            Admin_pw=self.pw.get()
            if Admin_number=="1" and Admin_pw=="1":
                self.page.destroy()
                self.lab3.pack_forget()
                AdminPage(self.root)
            else:
                showinfo(title='错误', message='账号或密码错误！')
        except:
                showinfo(title='错误',message='输入错误，请重新输入！')
                
    def admin_loginChecks(self):
        try:
            number=self.number.get()
            if number=="":
                showinfo(title="错误",message='请输入账号！')
            else:
                a=cxk(number)
                if(a <= 150):  #若差度在100内，可通过验证
                    self.page.destroy()
                    self.lab3.pack_forget()
                    AdminPage(self.root)
                elif (a==200.0):
                    showinfo(title='错误',message='无该人脸信息，请先进行人脸注册！')
                else:
                    showinfo(title='错误',message="没有通过验证！ 误差值为：%4.2f" % a)
        except:
            showinfo(title='错误',message='输入错误，请重新输入！')