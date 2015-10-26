# -*- coding: utf-8 -*-
#
# @author CoolYan

import sys
import pickle
import re

def main(argv):
    if len(argv) < 1:
        print("Input Error! usage: python wordquery.py inputwords.txt")
        return 0
    file_name = argv[0]
    if len(argv) > 1:
        read_file = argv[1]
    else:
        read_file = "my_dictionary.pk1"
    try:
        f = open(read_file, 'rb')
        my_directional = pickle.load(f)
        f.close()
        """
        if len(my_directional) < 100:
            print(my_directional)
        else:
            print("Total Len:", len(my_directional))
        """
        f = open(file_name)
        for line in f:
            strs = ""
            for i in line:
                if ('a' <= i <= 'z') or ('A' <= i <= 'Z'):
                    strs += i
            if strs.lower() in my_directional:
                lists = my_directional[strs.lower()]
                for j in range(len(lists) - 1):
                    print(lists[j], ", ", end="")
                print(lists[ - 1])
            else:
                print("")
        f.close()
    except:
        print("An Error Ocuuered:", sys.exc_info()[0])


    return 0


if __name__ == '__main__':
    try:
        exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        exit(0)

