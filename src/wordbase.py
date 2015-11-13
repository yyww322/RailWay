# -*- coding: utf-8 -*-
#
# @author CoolYan

import sys
import profile

from index_generator import IndexGenerator


def main(argv):
    if len(argv) < 1:
        print("Input Error! usage: python wordbase.py inputwords.txt savefilename")
        return 0
    file_name = argv[0]
    if len(argv) > 1:
        save_file = argv[1]
    else:
        save_file = "my_dictionary.pk1"
    generator = IndexGenerator(file_name, save_file)
    generator.begin_sort()
    return 0


if __name__ == '__main__':
    try:
        exit(main(sys.argv[1:]))
    except KeyboardInterrupt:
        exit(0)

