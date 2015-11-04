# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'

import os
from time import sleep
from tkinter import *
from do_Excel import *

# 文件遍历系统GUI


class DirList(object):
    def __init__(self, initdir = None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1')
        self.label.pack()
        self.cwd = StringVar(self.top)
        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold'))
        self.dirl.pack()
        # gui程序的核心，dirs（列表框）包含了被列目录的文件列表
        # 列表框用bind()方法把回调函数(setDirAndGo)和列表项绑定起来
        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb.config(command=self.dirs.yview)
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()
        # 文本框让用户输入目录名，转到想去的目录，在列表框中显示文件
        # 增加了一个Return或Enter键的绑定
        self.dirn = Entry(self.top, width=50,textvariable=self.cwd)
        self.dirn.bind('<Double-1>', self.doLS)
        self.dirn.pack()
        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear',
                          command=self.clrDir,
                          activeforeground='red',
                          activebackground='blue')
        self.ls = Button(self.bfm, text='List Directory',
                         command=self.doLS,
                         activeforeground='white',
                         activebackground='green')
        self.quit = Button(self.bfm, text='Quit',
                           command=self.top.quit,
                           activeforeground='white',
                           activebackground='green')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        # 初始化了GUI程序，程序从当前目录开始
        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    # 清空列表
    def clrDir(self, ev=None):
        self.cwd.set('')

    # 设置目录并显示
    def setDirAndGo(self, ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check1 = self.dirs.get(self.dirs.curselection())
        if check1[0] == '<' and check1[-1] == '>':
            check = check1[1:-1]
        else:
            check = check1[0:]
        if not check:
            check = os.curdir
        self.cwd.set(check)
        self.doLS()

    # 整个GUI程序的关键，负责所有安全性检查。如果正确，调用os.listdir()来取得新的文件集合
    # 并替换列表框中的列表
    def doLS(self, ev=None):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir

        if not os.path.exists(tdir):
            error = tdir + ': no such file'
        elif not os.path.isdir(tdir):
            file_name = tdir.split('.')[0] + '.xls'
            error = tdir + ': Translate into an Excel File'
            #写入excel表内容
            work = OperateExcel(3, 4, file_name)
            for i in range(3):
                for j in range(4):
                    work.set_data(i, j, i * 10 + j)
            work.write_data('1', 1, 1)
        #将来可以在这里添加文件处理功能
        if error:
            self.cwd.set(error)
            tdir = os.curdir
            sleep(2)
            """if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
                self.cwd.set(self.last)
                self.dirs.config(selectbackground='LightSkyBlue')
                self.top.update()
                return
            else:
                return
            """
        else:
            self.cwd.set('FETCHING DIRECTORY CONTENTS...')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)
        self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        #先显示目录，再显示文件
        for eachFile in dirlist:
            if os.path.isdir(eachFile):
                self.dirs.insert(END, '<' + eachFile + '>')
                self.cwd.set(os.curdir)
        for eachFile in dirlist:
            if os.path.isfile(eachFile):
                self.dirs.insert(END, eachFile)
                self.cwd.set(os.curdir)
                self.dirs.config(selectbackground='LightSkyBlue')

