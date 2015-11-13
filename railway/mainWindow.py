# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import os
from time import sleep
from tkinter import *
from myFrames import *

class  MainWindow(object):
    def __init__(self, showtype = 0):
        self.top = Tk()
        self.top.wm_title("限界仪后处理程序")
        """禁止缩放
        self.top.wm_resizable(FALSE, FALSE)"""
        self.file_frame = FileFrame(self.top)
        self.file_frame.grid(0, 0, W)
        self.big_frame = Frame(self.top)
        self.big_frame.grid(row=1, column=0, sticky=W)
        self.type_choose_frame = TypeChooseFrame(self.big_frame)
        self.type_choose_frame.grid(0, 1, W)

        self.in_big_frame = Frame(self.big_frame)
        self.in_big_frame.grid(row=0, column=0, sticky=W)
        self.limit_frame = LimitFrame(self.in_big_frame)
        self.limit_frame.grid(0, 0, N)
        self.save_frame = SaveButton(self.in_big_frame)
        self.save_frame.grid(1, 0, N)


    def show(self):
        self.top.mainloop()

    def button1(self):
        self.file_entry1.delete(0, len(self.file_entry1.get()))


