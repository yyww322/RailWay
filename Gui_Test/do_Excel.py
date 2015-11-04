# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


import sys
import xlwt


class OperateExcel(object):
    def __init__(self, rows, cols, work_file=''):
        self.work_file_name = work_file
        self.data = [[0 for col in range(cols)] for row in range(rows)]
        self.rows = rows
        self.cols = cols

    def set_file_name(self, file_name):
        self.work_file_name = file_name

    def write_data(self, name='dataSheet', row_start=0, col_start=0):
        """写入数据,data为符合条件的数据列表，name表示指定的哪三个列，
        file_name表示文件名，后面两个参数是写入的格子数偏移量"""
        file = xlwt.Workbook()
        table = file.add_sheet(name, cell_overwrite_ok=True)
        l = 0   # 表示行
        for line in self.data:
            c = 0 	# 表示一行下的列数
            for col in line:
                table.write(l + row_start, c + col_start, line[c])
                c += 1
            l += 1
        file.save(self.work_file_name)
        return True

    def set_data(self, row, col, data):
        self.data[row][col] = data

    def get_data(self, row, col):
        return self.data[row][col]

    def get_row(self):
        return self.rows

    def get_col(self):
        return self.cols

