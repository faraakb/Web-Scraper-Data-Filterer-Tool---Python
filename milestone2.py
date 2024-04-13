import csv

def convertToDictionaries(keys, values):
    newDict = {}
    final = []
    idx = 0
    for lists in values:
        while idx<len(lists):
            for k in keys:
                newDict[k] = lists[idx]
                idx+=1
            final.append(newDict)
        idx = 0
        newDict = {}
    return final
    
            



def loadRecords(filename):
    final = []
    with open(filename) as f:
        reader = csv.reader(f)
        header = next(reader)
        for line in reader:
            add = []
            for x in range(len(line)):
                add.append(line[x])
            final.append(add)
    return final




def convertToLists(keys, lod):
    final= []
    add = []
    for dicts in lod:
        for k in keys:
             for x in dicts.keys():
                if (k == x):
                    add.append(dicts[x])
    
                if (k not in dicts.keys()):
                    add.append("")
                    break
        final.append(add)
        add = []
    return final


def writeRecords(filename, records):
    with open(filename, "a") as f:
        for lists in records:
            writer = csv.writer(f)
            writer.writerow(lists)


        
    
    
    


                    
