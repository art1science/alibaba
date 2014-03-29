#!/usr/bin/python


import string
import math
import operator


def similarity(x,y):
    ret = 0
    for i in range(len(x)):
        ret = ret + math.pow(x[i] - y[i],2)
    return math.sqrt(ret)

def choose_top(k,i,data):
    base = data[i]
    ret = []
    index = {}
    for j in range(len(data)):
        if j != i:
            index[str(j)] = similarity(data[j],base)
    sorted_index = sorted(index.iteritems(), key=operator.itemgetter(1))
    for item in sorted_index:
        ret.append(int(item[0]))
    return ret[0:k]

if __name__ == "__main__":
    threshold = 2
    #3 means choose the one the user see and try to buy
    k = 5
    #choose the top 5 best likelihood person
    brand = []
    temp = {}
    f = open("brand_id")
    for line in f.readlines():
        temp[line.strip()] = 0
    f.close()
    for item in temp:
        brand.append(item)

    user = []
    data = []
    f = open("user_brand")
    for line in f.readlines():
        temp1 = string.split(line.strip(), ",")
        user.append(temp1[0])
        list = []
        for i in range(1,len(temp1),1):
            list.append(int(temp1[i]))
        data.append(list)
    f.close()

    for i in range(len(data)):
        result = user[i] + "\t"
        ret = choose_top(k,i,data)
        #for u in ret:
        #    print user[u]
        #print ret
        for j in ret:
            for n in range(len(data[j])):
                if data[j][n] > threshold:
                    result = result + brand[n] + ","
        print result[:-1]


