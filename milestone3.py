import milestone1
import milestone2
import os
import urllib.request as ur
import json
import matplotlib.pyplot as plt
def cacheAndLoadData(filename):
    keys = ['title','category','type','medium','frame','photo_url_link','artist', 'site','street_address','city','zip_code','state','latitude','longitude']
    if not os.path.isfile(filename):
        response = ur.urlopen("https://data.buffalony.gov/resource/6xz2-syui.json")
        content = response.read().decode()
        fin = json.loads(content)
        x = milestone2.convertToLists(keys, fin)
        x.insert(0,keys)
        milestone2.writeRecords(filename, x)
    e = milestone2.loadRecords(filename)
    return milestone2.convertToDictionaries(keys, e)

def cleanData(data):
    for dicts in data:
        for x in dicts.keys():
            if 'category' == x:
                if dicts[x] == "PAINTINGS":
                    dicts[x] = "PAINTING"
                if dicts[x] == "DECORATIVE OBJECTS":
                    dicts[x] = "DECORATIVE OBJECT"
                if dicts[x] == "GRAPHICS" or dicts[x] == "GRAPHIC" or dicts[x] == "GRAPHICS ARTS":
                    dicts[x] = "GRAPHIC ARTS"


def plotPieForKey(key, data):
    cleanData(data)
    labels = []
    vals = []
    x = milestone1.computeFrequency(key, data)
    for y in x.keys():
        labels.append(y)
    for x in x.values():
        vals.append(x)
    plt.pie(vals, labels = labels)
    plt.show()

def plotBarForKey(key, data):
    cleanData(data)
    labels = []
    vals = []
    x = milestone1.computeFrequency(key, data)
    for y in x.keys():
        labels.append(y)
    for x in x.values():
        vals.append(x)
    plt.barh(labels, vals)
    plt.show()


def plotFilteredBarForKey(key, fkey, fval, data):
    cleanData(data)
    labs = []
    vals = []
    x = milestone1.filterByKey(fkey, fval, data)
    y = milestone1.computeFrequency(key, x)
    for e in y.keys():
        labs.append(e)
    for u in y.values():
        vals.append(u)
    plt.barh(labs,vals)
    plt.show()



