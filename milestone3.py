import milestone1 as m1
import milestone2 as m2
import os
import urllib.request as ur
import json
import matplotlib.pyplot as pt

def cacheAndLoadData(file):
    keys=['title','category','type','medium','frame','photo_url_link','artist','site','street_address','city','zip_code','state','latitude','longitude']
    if not os.path.isfile(file):
        url = "https://data.buffalony.gov/resource/6xz2-syui.json"
        response = ur.urlopen(url)
        content = response.read().decode()
        converted=json.loads(content)
        records=m2.convertToLists(keys,converted)
        records.insert(0,keys)
        m2.writeRecords(file,records)
    load=m2.loadRecords(file)
    return m2.convertToDictionaries(keys,load)

def cleanData(data):
    for item in data:
        if (item["category"][-1].lower()=="s"):
            temp=item["category"][:len(item["category"])-1]
            item["category"]=temp
    return None

def plotPieForKey(key,data):
    array=m1.computeFrequency(key,data)
    pt.pie(array.values(),labels=array.keys())
    pt.show()
    return None

def plotBarForKey(key,data):
    array=m1.computeFrequency(key,data)
    pt.barh(list(array.keys()),list(array.values()))
    pt.show()
    return None

def plotFilteredBarForKey(key,fkey,fval,data):
    filtered=m1.filterByKey(fkey,fval,data)
    array=m1.computeFrequency(key,filtered)
    pt.barh(list(array.keys()),list(array.values()))
    pt.show()
    return None

print(cacheAndLoadData("out.csv"))

url = "https://data.buffalony.gov/resource/6xz2-syui.json"
response = ur.urlopen(url)
content = response.read().decode()
keys=['title','category','type','medium','frame','photo_url_link','artist',
'site','street_address','city','zip_code','state','latitude','longitude']
converted=json.loads(content)
cleanData(converted)
plotPieForKey("category",converted)
plotBarForKey("category",converted)
plotFilteredBarForKey('type', 'category', 'PAINTING',converted)
