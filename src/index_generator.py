# -*- coding: utf-8 -*-
#
# @author CoolYan

import pickle
import sys
import re


class IndexGenerator(object):

    def __init__(self, read_file, save_file = "my_dictionary.pk1"):
        self.open_file = read_file
        self.save_file = save_file
        self.my_str = ""
        self.my_direction = {}
        self.word_count = 0

    def get_str(self, file_name):
        try:
            f = open(file_name)
            self.my_str = f.read()
        except FileNotFoundError:
            print("File Not Found")
            exit(0)
        except:
            print("An Error happened:", sys.exc_info()[0])
            exit(0)
        finally:
            f.close()

    def gen_directionary(self):
        word = ''
        self.word_count = 1
        """
            从头循环到尾部,把所有英文字母提取出来,变成小写,如果不是英文字母则认为是断开
            断开后如果字长大于等于2个字母认为是一个英文单词,将其序号存入字典,并且单词序号计数器加1
            如果此前此单词没有存在于字典内,则先将其表明为列表存储形式才能添加序号入列表
            本程序只需要从头至尾循环一次即可完成这些功能
            最后一个字符如果不是符号的话，还需要额外存储一下
        """
        """
        for i in range(len(self.my_str)):
            if 'a' <= self.my_str[i] <= 'z':
                word += self.my_str[i]
            else:
                if 'Z' >= self.my_str[i] >= 'A':
                    word += self.my_str[i].lower()
                else:
                    if len(word) >= 1:
                        self.save_directionary(word, word_count)
                        word_count += 1
                    word = ''
        if len(word) >= 1:
            self.save_directionary(word, word_count)
        self.word_count = word_count
        """
        words = re.split('[^a-zA-Z]+', self.my_str)
        for word in words:
            self.save_directionary(word.lower(), self.word_count)
            self.word_count += 1

    def save_directionary(self, word, word_count):
        if len(word) >= 1:
            if word in self.my_direction:
                self.my_direction[word].append(word_count)
            else:
                self.my_direction[word] = []
                self.my_direction[word].append(word_count)

    def save_dir_to_file(self):
        try:
            f = open(self.save_file, 'wb')
            pickle.dump(self.my_direction, f)
        except FileNotFoundError:
            print("File Not Found")
            exit(0)
        except:
            print("An Error happened:", sys.exc_info()[0])
            exit(0)
        finally:
            f.close()

    def begin_sort(self):
        self.get_str(self.open_file)
        self.gen_directionary()
        self.save_dir_to_file()
        print("Total Vocabulary:", len(self.my_direction))
        print("Total Words:", self.word_count)
