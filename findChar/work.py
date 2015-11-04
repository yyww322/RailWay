# -*- coding: utf-8 -*-
# __author__ = 'toshiba'

import sys


def main(argv):
    if len(argv) < 1:
        print("Input Error! usage: python 需要转换的中文 wordFile.txt")
        return 0
    input_str = argv[0]
    if len(argv) > 1:
        read_file = argv[1]
    else:
        read_file = "workChar.txt"
    try:
        f = open(read_file, 'r', -1, 'utf-8')
        my_directionary = {}
        for line in f:
            datas = line.replace('\t', ' ').split()
            if len(datas) >= 3:
                if datas[0] == "﻿建":
                     my_directionary['建'] = [datas[1], datas[2]]
                else:
                     my_directionary[datas[0]] = [datas[1], datas[2]]
    except:
        print("An Error Ocuuered:", sys.exc_info()[0])
    finally:
        f.close()
    out_str = ''
    out_num = ''
    for word in input_str:
        if word in my_directionary:
            out_str += my_directionary[word][1]
            out_num += str(my_directionary[word][0])
        else:
            out_str += '?'
            out_num += '?'
    print("Use_ChineseArray_diaplay24x24(X, Y,", len(input_str), ",", out_num, ",", "\"" + out_str + "\"", ", COLOR3, 0xffff, 4, 0);  //" + input_str)
    return 0

if __name__ == '__main__':
    try:
        exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        exit(0)
