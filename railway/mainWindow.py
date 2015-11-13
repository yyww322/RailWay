# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import os
from time import sleep
from tkinter import *

class  MainWindow(object):
    def __init__(self):
        self.top = Tk()
        self.top.wm_title("限界仪后处理程序")
        """禁止缩放
        self.top.wm_resizable(FALSE, FALSE)"""
        self.lab1 = Label(self.top, text="This is a label")
        self.text1 = Text(self.top, )
        self.lab1.pack()
        self.text1.pack()

    def show(self):
        self.top.mainloop()
