def getValuesForKey(key,records):
    value_list=[]
    for dic in records:
        for key2 in dic.keys():
            if key in dic:
                if (key2 == key):
                    if dic[key2] not in value_list:
                        value_list.append(dic[key2])
    return value_list

def valueInDict(key,value,dic):
    if key in dic:
        if (dic[key]==value):
            return True
    return False

def countMatchesByKey(key,value,records):
    num=0
    for dic in records:
        judge=valueInDict(key,value,dic)
        if (judge):
            num+=1
    return num

def countMatchesByKeys(key1,value1,key2,value2,records):
    num=0
    for dic in records:
        judge1=valueInDict(key1,value1,dic)
        judge2=valueInDict(key2,value2,dic)
        if (judge1 and judge2):
            num+=1
    return num

def filterByKey(key,value,records):
    master=[]
    for dic in records:
        judge=valueInDict(key,value,dic)
        if (judge):
            master.append(dic)
    return master


def computeFrequency(key,records):
    master={}
    value_list=[]
    for dic in records:
        for key2 in dic.keys():
            if key in dic:
                if (key2 == key):
                    value_list.append(dic[key2])
    for value in value_list:
        if value not in master:
            master[value]=1
        else:
            number=master[value]+1
            master[value]=number
    return master
