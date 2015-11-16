# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'


class SystemData(object):
    def __init__(self, file_name="systemDate.txt"):
        self.title = ["OPEN_FILE:", "MODEL_FILE:", "CURVE_FILE:", "H_LIMIT:", "V_LIMIT:"
                      , "POS_X:", "POS_Y:", "RAIL_TYPE:", "ROOF_H:", "ROOF_V:", "PILLAR_H:"]
        self.open_file_name = ""
        self.model_file_name = ""
        self.curve_file_name = ""
        self.h_limit = 0.0
        self.v_limit = 0.0
        self.pos_x = 100
        self.pos_y = 100
        self.rail_type = ""
        self.roof_h_limit = 0.0
        self.roof_v_limit = 0.0
        self.pillar_h_limit = 0.0
        # 轨道参数不存储在文件中，内存中使用
        self.rail_data = []
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
                if temp1[0] == self.title[8]:
                    if len(temp1) > 1:
                        self.roof_h_limit = temp1[1]
                if temp1[0] == self.title[9]:
                    if len(temp1) > 1:
                        self.roof_v_limit = temp1[1]
                if temp1[0] == self.title[10]:
                    if len(temp1) > 1:
                        self.pillar_h_limit = temp1[1]

        except:
            self.file = open(file_name, 'x')
            self.save_data()
        finally:
            self.file.close()

    def save_data(self, open_file_name="", model_file_name="", curve_file_name="",
                  h_limit=0, v_limit=0, pos_x=100, pos_y=100, rail_type="", roof_h=0.0, roof_v=0.0, pillar_h=0.0):
        self.file.seek(0)
        self.file.write(self.title[0] + ' ' + open_file_name + '\n')
        self.file.write(self.title[1] + ' ' + model_file_name + '\n')
        self.file.write(self.title[2] + ' ' + curve_file_name + '\n')
        self.file.write(self.title[3] + ' ' + str(h_limit) + '\n')
        self.file.write(self.title[4] + ' ' + str(v_limit) + '\n')
        self.file.write(self.title[5] + ' ' + str(pos_x) + '\n')
        self.file.write(self.title[6] + ' ' + str(pos_y) + '\n')
        self.file.write(self.title[7] + ' ' + rail_type + '\n')
        self.file.write(self.title[8] + ' ' + str(roof_h) + '\n')
        self.file.write(self.title[9] + ' ' + str(roof_v) + '\n')
        self.file.write(self.title[10] + ' ' + str(pillar_h) + '\n')

    def record_sys(self, file_name="systemDate.txt"):
        self.file = open(file_name, "w")
        self.save_data(self.open_file_name, self.model_file_name, self.curve_file_name,
                       self.h_limit, self.v_limit, self.pos_x, self.pos_y, self.rail_type, self.roof_h_limit
                       , self.roof_v_limit, self.pillar_h_limit)
        self.file.close()
