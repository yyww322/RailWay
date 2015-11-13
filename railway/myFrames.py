# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from systemData import *


sys_data = SystemDate()


class FileFrame(object):
    global sys_data

    def __init__(self, master, texts="操作文件"):
        self.file_frame = LabelFrame(master, text=texts)

        self.file_lab1 = Label(self.file_frame, text="操作文件")
        self.file_lab1.grid(row=0, column=0, sticky=W)
        self.file_lab2 = Label(self.file_frame, text="模板文件")
        self.file_lab2.grid(row=1, column=0, sticky=W)
        self.file_lab3 = Label(self.file_frame, text="轨道参数文件")
        self.file_lab3.grid(row=2, column=0, sticky=W)
        self.file_entry1 = Entry(self.file_frame)
        self.file_entry1.grid(row=0, column=1, sticky=E)
        self.file_entry1.insert(0, "请选择文件")
        self.file_entry2 = Entry(self.file_frame)
        self.file_entry2.grid(row=1, column=1, sticky=E)
        self.file_entry3 = Entry(self.file_frame)
        self.file_entry3.grid(row=2, column=1, sticky=E)
        self.file_but1 = Button(self.file_frame, text="选择", command=self.button1)
        self.file_but1.grid(row=0, column=2, sticky=E)
        self.file_but2 = Button(self.file_frame, text="选择", command=self.button2)
        self.file_but2.grid(row=1, column=2, sticky=E)
        self.file_but3 = Button(self.file_frame, text="选择", command=self.button3)
        self.file_but3.grid(row=2, column=2, sticky=E)

        self.file_entry2.insert(0, sys_data.model_file_name)
        self.file_entry3.insert(0, sys_data.curve_file_name)

        self.opening = 0

    def grid(self, rows, columns, stickys):
        self.file_frame.grid(row=rows, column=columns, sticky=stickys)

    def button1(self):
        if self.opening == 0:
            self.opening += 1
            file = askopenfilename(defaultextension=".txt", initialdir=sys_data.open_file_name)
            if file != "":
                self.file_entry1.delete(0, len(self.file_entry1.get()))
                self.file_entry1.insert(0, file)
                sys_data.open_file_name = file
            self.opening -= 1

    def button2(self):
        if self.opening == 0:
            self.opening += 1
            file = askopenfilename(defaultextension=".xls", initialdir=sys_data.model_file_name)
            if file != "":
                self.file_entry2.delete(0, len(self.file_entry2.get()))
                self.file_entry2.insert(0, file)
                sys_data.model_file_name = file
            self.opening -= 1

    def button3(self):
        if self.opening == 0:
            self.opening += 1
            file = askopenfilename(defaultextension=".xls", initialdir=sys_data.curve_file_name)
            if file != "":
                self.file_entry3.delete(0, len(self.file_entry3.get()))
                self.file_entry3.insert(0, file)
                sys_data.curve_file_name = file
            self.opening -= 1


class TypeChooseFrame(object):
    global sys_data

    def __init__(self, master, texts="请选择轨道类型"):
        self.type_choose_frame = LabelFrame(master, text=texts)
        self.rail_type = self.get_rail_types()
        i = 0
        self.var = IntVar()
        self.radio = []
        for rails in self.rail_type:
            self.radio.append(Radiobutton(self.type_choose_frame, text=rails[0], variable=self.var,
                                          value=i, command=self.sel))
            self.radio[i].grid(row=i, column=0, sticky=W)
            i += 1
        i = 0
        for types in self.rail_type:
            if types[0] == sys_data.rail_type:
                self.radio[i].invoke()
                break
            i += 1
        self.label = Label(self.type_choose_frame)
        self.label.grid(row=i, column=0, sticky=W)

    def grid(self, rows, columns, stickys):
        self.type_choose_frame.grid(row=rows, column=columns, sticky=stickys)

    def get_rail_types(self, file_name="RailType.txt"):
        try:
            file = open(file_name, 'r')
            rail_data = []
            for line in file:
                rail_data.append(line.strip("\n").split())
        except:
            rail_data = [["38", 134, 114, 68, 13], ["43", 140, 114, 70, 14.5], ["50", 152, 132, 70, 15.5],
                        ["60", 176, 150, 73, 16.5], ["75", 192, 150, 75, 20]]
            file = open(file_name, 'x')
            for line in rail_data:
                write_string = ""
                for elements in line:
                    write_string += (str(elements) + ' ')
                file.write(write_string[0: -1] + '\n')

        finally:
            file.close()
            return rail_data

    def sel(self):
        """selection = "You selected the option " + str(self.var.get())
        self.label.config(text=selection)"""
        sys_data.rail_type = self.rail_type[self.var.get()][0]


class LimitFrame(object):
    global sys_data

    def __init__(self, master, texts="请输入限界值"):
        self.limit_frame = LabelFrame(master, text=texts)
        self.lab1 = Label(self.limit_frame, text="水平限界(m)")
        self.lab2 = Label(self.limit_frame, text="垂直限界(m)")
        self.ent1 = Entry(self.limit_frame)
        self.ent2 = Entry(self.limit_frame)
        self.lab1.grid(row=0, column=0, sticky=W)
        self.ent1.grid(row=0, column=1, sticky=E)
        self.lab2.grid(row=1, column=0, sticky=W)
        self.ent2.grid(row=1, column=1, sticky=E)
        self.ent1.insert(0, sys_data.h_limit)
        self.ent2.insert(0, sys_data.v_limit)
        self.ent1.bind("<FocusOut>", self.ent1_input)
        self.ent2.bind("<FocusOut>", self.ent2_input)

    def grid(self, rows, columns, stickys):
        self.limit_frame.grid(row=rows, column=columns, sticky=stickys)

    def ent1_input(self, event):
        str1 = self.ent1.get()
        if len(str) > 0:
            try:
                sys_data.h_limit = float(str1)
            except:
                sys_data.h_limit = 0.0

    def ent2_input(self, event):
        str1 = self.ent2.get()
        if len(str) > 0:
            try:
                sys_data.v_limit = float(str1)
            except:
                sys_data.v_limit = 0.0


class SaveButton(object):
    global sys_data

    def __init__(self, master):
        self.save_frame = Frame(master)
        self.but1 = Button(self.save_frame, text="保存", command=self.button1)
        self.but2 = Button(self.save_frame, text="退出", command=self.button2)
        self.but1.grid(row=0, column=0)
        self.but2.grid(row=0, column=1)

    def grid(self, rows, columns, stickys):
        self.save_frame.grid(row=rows, column=columns, sticky=stickys)

    def button1(self):
        file = asksaveasfilename(defaultextension=".xls")

    def button2(self):
        sys_data.record_sys()
        os._exit(0)
