def getValuesForKey(key, records):
    aList = []
    for dicts in records:
        for x in dicts.keys():
            if (x == key):
                e = dicts[x]
                if (e not in aList):
                    aList.append(e)
    return aList
    

def countMatchesByKey(key, value, records):
    count = 0
    for dicts in records:
        for x in dicts.keys():
            if (x == key and dicts[x] ==  value):
                count+=1
    return count


def countMatchesByKeys(key1, value1, key2, value2, records):
    count = 0
    for dicts in records:
        if (key1 in dicts.keys() and dicts[key1] == value1) and (key2 in dicts.keys() and dicts[key2]==value2):
            count+=1
    return count


def filterByKey(key, value, records):
    aList = []
    for dicts in records:
        for x in dicts:
            if (x==key and dicts[x] == value):
                aList.append(dicts)
    return aList


def computeFrequency(key, records):
    aDict = {}
    aList = getValuesForKey(key,records)
    for x in range(len(aList)):
        val = countMatchesByKey(key, aList[x], records)
        aDict[aList[x]] = val
    return aDict

