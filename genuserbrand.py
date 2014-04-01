#!/usr/bin/python


import string

def weight(type):
    if type == "3":
        return int(type) + 100
    elif type == "2":
        return int(type) + 50
    else:
        return int(type)+1


if __name__ == "__main__":
    user = {}
    f = open("trick.csv")
    for line in f.readlines():
        temp = string.split(line.strip(), ",")
        if user.has_key(temp[0]):
            if(user[temp[0]].has_key(temp[1])):
                user[temp[0]][temp[1]] = user[temp[0]][temp[1]] + weight(temp[2])
            else:
                user[temp[0]][temp[1]] = weight(temp[2])
        else:
            brand = {}
            brand[temp[1]] = weight(temp[2]) 
            user[temp[0]] = brand
        #if temp[0] == "4025000":
        #    print user[temp[0]]
    f.close()
    
    vec = []
    f = open("brand_id")
    for line in f.readlines():
        vec.append(line.strip())
    f.close()

    for u in user:
        result = u + ","
        for i in range(len(vec)):
            if user[u].has_key(vec[i]):
                #if u == "8949750":
                #    print i
                result = result + str(user[u][vec[i]]) + ","
            else:
                result = result + "0,"
        if result[-1] == "\t":
            print result
        else:
            print result[:-1]
            







