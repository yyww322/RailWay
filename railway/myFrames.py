# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import os
import shutil
from tkinter import *
from tkinter.filedialog import *
from tkinter.ttk import *
from systemData import *
from readData import *
from do_Excel import *

sys_data = SystemData()


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
                sys_data.rail_data = types
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
        self.lab1 = Label(self.limit_frame, text="铁轨水平限界(m)")
        self.lab2 = Label(self.limit_frame, text="铁轨垂直限界(m)")
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

        self.lab3 = Label(self.limit_frame, text="雨棚水平限界(m)")
        self.lab4 = Label(self.limit_frame, text="雨棚垂直限界(m)")
        self.ent3 = Entry(self.limit_frame)
        self.ent4 = Entry(self.limit_frame)
        self.lab3.grid(row=2, column=0, sticky=W)
        self.ent3.grid(row=2, column=1, sticky=E)
        self.lab4.grid(row=3, column=0, sticky=W)
        self.ent4.grid(row=3, column=1, sticky=E)
        self.ent3.insert(0, sys_data.roof_h_limit)
        self.ent4.insert(0, sys_data.roof_v_limit)
        self.ent3.bind("<FocusOut>", self.ent3_input)
        self.ent4.bind("<FocusOut>", self.ent4_input)

        self.lab5 = Label(self.limit_frame, text="立柱水平限界(m)")
        self.ent5 = Entry(self.limit_frame)
        self.lab5.grid(row=4, column=0, sticky=W)
        self.ent5.grid(row=4, column=1, sticky=E)
        self.ent5.insert(0, sys_data.pillar_h_limit)
        self.ent5.bind("<FocusOut>", self.ent5_input)

    def grid(self, rows, columns, stickys):
        self.limit_frame.grid(row=rows, column=columns, sticky=stickys)

    def ent1_input(self, event):
        str1 = self.ent1.get()
        if len(str1) > 0:
            try:
                sys_data.h_limit = float(str1)
            except:
                sys_data.h_limit = 0.0

    def ent2_input(self, event):
        str1 = self.ent2.get()
        if len(str1) > 0:
            try:
                sys_data.v_limit = float(str1)
            except:
                sys_data.v_limit = 0.0

    def ent3_input(self, event):
        str1 = self.ent3.get()
        if len(str1) > 0:
            try:
                sys_data.roof_h_limit = float(str1)
            except:
                sys_data.roof_h_limit = 0.0

    def ent4_input(self, event):
        str1 = self.ent4.get()
        if len(str1) > 0:
            try:
                sys_data.roof_v_limit = float(str1)
            except:
                sys_data.roof_v_limit = 0.0

    def ent5_input(self, event):
        str1 = self.ent5.get()
        if len(str1) > 0:
            try:
                sys_data.pillar_h_limit = float(str1)
            except:
                sys_data.pillar_h_limit = 0.0


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
        self.readData = ReadData(sys_data.open_file_name)
        # 如果有有效数据就显示输入文件名，同时将文件名整理为.xls的后缀格式
        if len(self.readData.all_data) > 0:
            file_name = asksaveasfilename(defaultextension=".xls")
        else:
            return
        if file_name == "":
            return
        if '.' in file_name:
            tmp1 = file_name.split('.')
            file_name = ""
            for chr in tmp1[0: -1]:
                file_name += chr + '.'
        file_name += "xls"
        file_name = file_name.split(".xls")
        j = 1
        for datas in self.readData.all_data:
            self.save_excel(datas, file_name[0] + '_' + str(j) + "组数据" +
                            datas.Platform + "站台" + datas.RailNum + "轨道")
            j += 1
        """excel_file = OperateExcel(file_name)
        excel_file.open_file()
        excel_file.write_one_data(2, 2, self.readData.all_data[0].Station)
        excel_file.write_one_data(2, 8, self.readData.all_data[0].Date)
        excel_file.write_one_data(3, 4, self.readData.all_data[0].Platform)
        excel_file.write_one_data(4, 3, self.readData.all_data[0].RailNum)
        excel_file.close_file()"""
        pass

    def save_excel(self, all_data, file_name):
        # 跟据数据大小以及长度创建数个excel文件，但仅操作一组数据
        file_name1 = file_name.split(".xls")
        rail_name = file_name1[0] + "_铁轨"
        roof_name = file_name1[0] + "_雨棚"
        pillar_name = file_name1[0] + "_立柱"
        # 保存铁轨数据
        i = len(all_data.railData)
        j = 1
        if i > 0:
            while i > 26:
                shutil.copy(sys_data.model_file_name, rail_name + str(j) + ".xls")
                excel_file = OperateExcel(rail_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, 26):
                    h_value = float(all_data.railData[(j - 1) * 26 + k][6]) + float(sys_data.rail_data[3]) + 1.435 / 2
                    v_value = float(all_data.railData[(j - 1) * 26 + k][2])
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.railData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, sys_data.v_limit)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, float(v_value) - float(sys_data.v_limit))
                excel_file.close_file()
                i -= 26
                j += 1
            # 如果i还有剩余的数据，填写入新的里面
            if i > 0:
                shutil.copy(sys_data.model_file_name, rail_name + str(j) + ".xls")
                excel_file = OperateExcel(rail_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, i):
                    h_value = float(all_data.railData[(j - 1) * 26 + k][6]) + float(sys_data.rail_data[3]) + 1.435 / 2
                    v_value = all_data.railData[(j - 1) * 26 + k][2]
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.railData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, sys_data.v_limit)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, float(v_value) - float(sys_data.v_limit))
                excel_file.close_file()
                i -= 26
                j += 1

        # 保存雨棚数据
        i = len(all_data.roofData)
        j = 1
        if i > 0:
            while i > 26:
                shutil.copy(sys_data.model_file_name, roof_name + str(j) + ".xls")
                excel_file = OperateExcel(roof_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, 26):
                    h_value = all_data.roofData[(j - 1) * 26 + k][3]
                    v_value = all_data.roofData[(j - 1) * 26 + k][2]
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.roofData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.roof_h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, sys_data.roof_v_limit)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.roof_h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, float(h_value) - float(sys_data.roof_v_limit))
                excel_file.close_file()
                i -= 26
                j += 1
            # 如果i还有剩余的数据，填写入新的里面
            if i > 0:
                shutil.copy(sys_data.model_file_name, roof_name + str(j) + ".xls")
                excel_file = OperateExcel(roof_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, i):
                    h_value = all_data.roofData[(j - 1) * 26 + k][3]
                    v_value = all_data.roofData[(j - 1) * 26 + k][2]
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.roofData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.roof_h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, sys_data.roof_v_limit)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, float(h_value) - float(sys_data.h_limit))
                excel_file.close_file()
                i -= 26
                j += 1

        # 保存立柱数据
        i = len(all_data.pillarData)
        j = 1
        if i > 0:
            while i > 26:
                shutil.copy(sys_data.model_file_name, pillar_name + str(j) + ".xls")
                excel_file = OperateExcel(pillar_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, 26):
                    h_value = float(all_data.pillarData[(j - 1) * 26 + k][3]) - \
                              float(all_data.pillarData[(j - 1) * 26 + k][6])
                    v_value = 0.0
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.pillarData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.pillar_h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, 0.0)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.pillar_h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, 0.0)
                excel_file.close_file()
                i -= 26
                j += 1
            # 如果i还有剩余的数据，填写入新的里面
            if i > 0:
                shutil.copy(sys_data.model_file_name, pillar_name + str(j) + ".xls")
                excel_file = OperateExcel(pillar_name + str(j) + ".xls")
                excel_file.open_file()
                excel_file.write_one_data(2, 2, all_data.Station)
                excel_file.write_one_data(2, 8, all_data.Date)
                excel_file.write_one_data(3, 4, all_data.Platform)
                excel_file.write_one_data(4, 3, all_data.RailNum)
                excel_file.write_one_data(34, 3, all_data.Name)
                for k in range(0, i):
                    h_value = float(all_data.pillarData[(j - 1) * 26 + k][3]) - \
                              float(all_data.pillarData[(j - 1) * 26 + k][6])
                    v_value = 0.0
                    # 点号
                    excel_file.write_one_data(7 + k, 1, all_data.pillarData[(j - 1) * 26 + k][0])
                    # 实测限界
                    excel_file.write_one_data(7 + k, 2, h_value)
                    # 实测高度
                    excel_file.write_one_data(7 + k, 3, v_value)
                    # 标准限界
                    excel_file.write_one_data(7 + k, 6, sys_data.pillar_h_limit)
                    # 标准高度
                    excel_file.write_one_data(7 + k, 7, 0.0)
                    # 侵蚀水平
                    excel_file.write_one_data(7 + k, 8, float(h_value) - float(sys_data.pillar_h_limit))
                    # 侵蚀高度
                    excel_file.write_one_data(7 + k, 9, 0.0)
                excel_file.close_file()
                i -= 26
                j += 1

    def button2(self):
        sys_data.record_sys()
        os._exit(0)
