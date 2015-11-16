# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import sys
import win32com.client


class OperateExcel(object):
    def __init__(self, work_file=''):
        self.work_file_name = work_file

    def set_file_name(self, file_name):
        self.work_file_name = file_name

    def open_file(self):
        self.xlApp = win32com.client.Dispatch('Excel.Application') #打开EXCEL，这里不需改动
        self.xlBook = self.xlApp.Workbooks.Open(self.work_file_name) #将D:\\1.xls改为要处理的excel文件路径

    def write_one_data(self, row, col, data, name='sheet1'):
        self.xlSht = self.xlBook.Worksheets(name) #要处理的excel页，默认第一页是‘sheet1’
        #aaa = xlSht.Cells(1,2).Value #可以用这种方法获取指定单元格的值
        self.xlSht.Cells(row, col).Value = data #可以用这种方法给指定的单元格赋值

    def close_file(self):
        self.xlBook.Close(SaveChanges=1) #完成 关闭保存文件
        del self.xlApp

