#!/usr/bin/python

import string


if __name__ == "__main__":
    dict = {}
    f = open("good.csv")
    for line in f.readlines():
        temp = string.split(line.strip(),",")
        if dict.has_key(str(temp[1])):
            dict[str(temp[1])] = dict[str(temp[1])] + 1
        else:
            dict[str(temp[1])] = 1
    f.close()
    for item in dict:
        print item

