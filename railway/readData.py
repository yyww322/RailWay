# -*- coding: utf-8 -*-
# __author__ = 'CoolYan'

import traceback


class DataStore(object):
    def __init__(self, temp=20, air=1013.25, station="", platform="", railnum="", date="", department="", name=""
                 , railtype="", baisx=0, biasy=0, biasz=0):
        self.Temp = temp
        self.AirPressure = air
        self.Station = station
        self.Platform = platform
        self.RailNum = railnum
        self.Date = date
        self.Department = department
        self.Name = name
        self.RailType = railtype
        self.BiasX = baisx
        self.BiasY = biasy
        self.BiasZ = biasz
        self.railData = []
        self.roofData = []
        self.pillarData = []

    def add_Rail(self, railData):
        for i in self.railData:
            if railData[0] == i[0]:
                for j in range(0, len(i)):
                    i[j] = railData[j]
                return
        self.railData.append(railData)

    def add_roof(self, roofData):
        for i in self.roofData:
            if roofData[0] == i[0]:
                for j in range(0, len(i)):
                    i[j] = roofData[j]
                return
        self.roofData.append(roofData)

    def add_Pillar(self, pillarData):
        for i in self.pillarData:
            if pillarData[0] == i[0]:
                for j in range(0, len(i)):
                    i[j] = pillarData[j]
                return
        self.pillarData.append(pillarData)


class ReadData(object):
    def __init__(self, file_name):
        self.env_title = ["Temp:", "AirPressure:", "Station:", "Platform:", "RailNum:"
                      , "Date:", "Department:", "Name:", "RailType:", "BiasX:", "BiasY:", "BiasZ:"]
        self.data_title = ["rail:", "roof:", "pillar:"]
        """0表示环境参数, 1表示实际数据"""
        self.flag = 0
        self.all_data = []
        self.temp_data = DataStore()
        try:
            self.file = open(file_name, 'r')
            for lines in self.file:
                lines = lines.strip('\n')
                temp1 = lines.split()
                if len(temp1) > 0:
                    if temp1[0] in self.env_title:
                        if self.flag != 0:
                            self.flag = 0
                            self.all_data.append(self.temp_data)
                            self.temp_data = DataStore()
                        if len(temp1) > 1:
                            if temp1[0] == self.env_title[0]:
                                self.temp_data.Temp = temp1[1]
                            if temp1[0] == self.env_title[1]:
                                self.temp_data.AirPressure = temp1[1]
                            if temp1[0] == self.env_title[2]:
                                self.temp_data.Station = temp1[1]
                            if temp1[0] == self.env_title[3]:
                                self.temp_data.Platform = temp1[1]
                            if temp1[0] == self.env_title[4]:
                                self.temp_data.RailNum = temp1[1]
                            if temp1[0] == self.env_title[5]:
                                self.temp_data.Date = temp1[1]
                            if temp1[0] == self.env_title[6]:
                                self.temp_data.Department = temp1[1]
                            if temp1[0] == self.env_title[7]:
                                self.temp_data.Name = temp1[1]
                            if temp1[0] == self.env_title[8]:
                                self.temp_data.RailType = temp1[1]
                            if temp1[0] == self.env_title[9]:
                                self.temp_data.BiasX = temp1[1]
                            if temp1[0] == self.env_title[10]:
                                self.temp_data.BiasY = temp1[1]
                            if temp1[0] == self.env_title[11]:
                                self.temp_data.BiasZ = temp1[1]

                if temp1[0] in self.data_title:
                    self.flag = 1
                    if len(temp1) > 1:
                        if temp1[0] == self.data_title[0]:
                            self.temp_data.add_Rail(temp1[1:])
                        if temp1[0] == self.data_title[1]:
                            self.temp_data.add_roof(temp1[1:])
                        if temp1[0] == self.data_title[2]:
                            self.temp_data.add_Pillar(temp1[1:])
            if self.flag == 1:
                self.all_data.append(self.temp_data)
        except Exception as e:
            print(e)
            pass
        finally:
            self.file.close()

