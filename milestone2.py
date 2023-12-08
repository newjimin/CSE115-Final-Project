import csv

def convertToDictionaries(keys,values):
    master=[]
    for value in values:
        temp={}
        for i in range(len(keys)):
            temp[keys[i]]=value[i]
        master.append(temp)
    return master

def loadRecords(file):
    master=[]
    with open (file,"r",newline="") as f:
        reader=csv.reader(f)
        headers=next(reader)
        for line in reader:
            temp=[]
            for x in range(len(headers)):
                temp.append(line[x])
            master.append(temp)
    return master

def convertToLists(key,lod):
    master=[]
    for dic in lod:
        temp=[]
        for key1 in key:
            if (key1 in dic.keys()):
                temp.append(dic[key1])
            else:
                temp.append("")
        master.append(temp)
    return master

                
def writeRecords(file,records):
    with open(file,"a",newline="") as f:
        writer = csv.writer(f)
        for record in records:
            writer.writerow(record)
    return None
