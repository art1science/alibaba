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
    #    if j != i:
        index[str(j)] = similarity(data[j],base)
    sorted_index = sorted(index.iteritems(), key=operator.itemgetter(1))
    for item in sorted_index:
        ret.append(int(item[0]))
    return ret[0:k]

def choose_itself(k,i,data):
    ret = []
    ret.append(i)
    return ret

if __name__ == "__main__":
    threshold = 3
    #3 means choose the one the user see and try to buy
    k = 1
    #choose the top 5 best likelihood person
    brand = []
    f = open("brand_id")
    for line in f.readlines():
        brand.append(line.strip())
    f.close()

    user = []
    data = []
    f = open("user_brand_trick")
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
        #ret = choose_top(k,i,data)
        ret = choose_itself(k,i,data)
        #for u in ret:
        #    print user[u]
        #print ret
        for j in ret:
            for n in range(len(data[j])):
                if data[j][n] >= threshold:
                    #if user[i] == "8949750":
                    #    print brand[n]
                    result = result + brand[n] + ","
        if(result[-1]) == "\t":
            print result
        else:
            print result[:-1]


