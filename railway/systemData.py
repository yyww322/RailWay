# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


class SystemDate(object):
    def __init__(self, file_name="systemDate.txt"):
        self.title = ["OPEN_FILE:", "MODEL_FILE:", "CURVE_FILE:", "H_LIMIT:", "V_LIMIT:"
                      , "POS_X:", "POS_Y:", "RAIL_TYPE:"]
        self.open_file_name = ""
        self.model_file_name = ""
        self.curve_file_name = ""
        self.h_limit = 0.0
        self.v_limit = 0.0
        self.pos_x = 100
        self.pos_y = 100
        self.rail_type = ""
        try:
            self.file = open(file_name, 'r')
            for lines in self.file:
                lines = lines.strip('\n')
                temp1 = lines.split(' ')
                if temp1[0] == self.title[0]:
                    if len(temp1) > 1:
                        self.open_file_name = temp1[1]
                if temp1[0] == self.title[1]:
                    if len(temp1) > 1:
                        self.model_file_name = temp1[1]
                if temp1[0] == self.title[2]:
                    if len(temp1) > 1:
                        self.curve_file_name = temp1[1]
                if temp1[0] == self.title[3]:
                    if len(temp1) > 1:
                        self.h_limit = temp1[1]
                if temp1[0] == self.title[4]:
                    if len(temp1) > 1:
                        self.v_limit = temp1[1]
                if temp1[0] == self.title[5]:
                    if len(temp1) > 1:
                        self.pos_x = temp1[1]
                if temp1[0] == self.title[6]:
                    if len(temp1) > 1:
                        self.pos_y = temp1[1]
                if temp1[0] == self.title[7]:
                    if len(temp1) > 1:
                        self.rail_type = temp1[1]

        except:
            self.file = open(file_name, 'x')
            self.save_data()
        finally:
            self.file.close()

    def save_data(self, open_file_name="", model_file_name="", curve_file_name="",
                  h_limit=0, v_limit=0, pos_x=100, pos_y=100, rail_type=""):
        self.file.seek(0)
        self.file.write(self.title[0] + ' ' + open_file_name + '\n')
        self.file.write(self.title[1] + ' ' + model_file_name + '\n')
        self.file.write(self.title[2] + ' ' + curve_file_name + '\n')
        self.file.write(self.title[3] + ' ' + str(h_limit) + '\n')
        self.file.write(self.title[4] + ' ' + str(v_limit) + '\n')
        self.file.write(self.title[5] + ' ' + str(pos_x) + '\n')
        self.file.write(self.title[6] + ' ' + str(pos_y) + '\n')
        self.file.write(self.title[7] + ' ' + rail_type + '\n')

    def record_sys(self, file_name="systemDate.txt"):
        self.file = open(file_name, "w")
        self.save_data(self.open_file_name, self.model_file_name, self.curve_file_name,
                       self.h_limit, self.v_limit, self.pos_x, self.pos_y, self.rail_type)
        self.file.close()
