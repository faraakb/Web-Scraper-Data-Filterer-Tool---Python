def getValuesForKey(key, records):
    aList = []
    for dicts in records:
        for x in dicts.keys():
            if (x == key):
                e = dicts[x]
                if (e not in aList):
                    aList.append(e)
    return aList
    
print(getValuesForKey("Artist", [{"Artist": "DaBaby"},{"Artist": "J-Cole"}]))

def countMatchesByKey(key, value, records):
    count = 0
    for dicts in records:
        for x in dicts.keys():
            if (x == key and dicts[x] ==  value):
                count+=1
    return count

print(countMatchesByKey("Artist", "DaBaby", [{"Artist": "DaBaby"},{"Artit": "J-Cole"}]))

e = [{"Artist": "DaBaby","Artist": "J-Cole"}]
def countMatchesByKeys(key1, value1, key2, value2, records):
    count = 0
    for dicts in records:
        if (key1 in dicts.keys() and dicts[key1] == value1) and (key2 in dicts.keys() and dicts[key2]==value2):
            count+=1
    return count

print(countMatchesByKeys("Artist", "J-Cole", "Artist", "J-Cole", e))
print(countMatchesByKeys("Genre", "Horror", "Rating", 5, [{'Title': 'Halloween', 'Runtime': 91, 'Year': 1978, 'Genre': 'Horror', 'Rating': 5}, {'Title': 'Friday the 13th', 'Runtime': 95, 'Year': 1980, 'Genre': 'Horror', 'Rating': 5}, {'Title': 'Nightmare on Elm Street', 'Runtime': 91, 'Year': 1984, 'Genre': 'Horror', 'Rating': 3}, {'Title': 'The Shape of Water', 'Runtime': 123, 'Year': 2017, 'Rating': 5}, {'Title': 'Swiss Army Man', 'Runtime': 137, 'Year': 2016, 'Genre': 'Comedy', 'Rating': 4}]))
print(countMatchesByKeys("Genre", "Comedy", "Rating", 4, [{'Title': 'Halloween', 'Runtime': 91, 'Year': 1978, 'Genre': 'Horror', 'Rating': 5}, {'Title': 'Friday the 13th', 'Runtime': 95, 'Year': 1980, 'Genre': 'Horror', 'Rating': 5}, {'Title': 'Nightmare on Elm Street', 'Runtime': 91, 'Year': 1984, 'Genre': 'Horror', 'Rating': 3}, {'Title': 'The Shape of Water', 'Runtime': 123, 'Year': 2017, 'Rating': 5}, {'Title': 'Swiss Army Man', 'Runtime': 137, 'Year': 2016, 'Genre': 'Comedy', 'Rating': 4}]))
print(countMatchesByKeys("Z", 1, "2", 1, [{'N': 6, 'E': 4, '1': 5, 'b': 2, 'C': 0, 'M': 4, 'Z': 1, '2': 0}, {'T': 8, 'R': 6, 'c': 3, '1': 7, 'Z': 0, 'j': 5, '2': 1}, {'M': 6, 'F': 2, 'q': 2, 't': 4, 'A': 3, 'Z': 0, '2': 1}, {'s': 8, 'L': 2, 'S': 0, '3': 7, 'D': 9, 'v': 2, 'Z': 1, '2': 1}, {'j': 4, 'L': 9, 'e': 2, 'E': 6, 'N': 2, 'Z': 1, '2': 0}]))
def filterByKey(key, value, records):
    aList = []
    for dicts in records:
        for x in dicts:
            if (x==key and dicts[x] == value):
                aList.append(dicts)
    return aList

print(filterByKey("Artist", "J-Cole", e))
print(filterByKey("H", 0, [{'D': 5, 'm': 5, '0': 4, '2': 3, 'P': 3, 'S': 3, 'H': 0}, {'V': 4, 'a': 1, 'e': 7, 'Z': 5, 'B': 7, 'H': 0}, {'M': 2, 'G': 9, '2': 2, 'D': 2, '8': 3, 'H': 2}, {'Z': 3, 'T': 9, '1': 5, '2': 1, 'b': 6, 'r': 5, 'p': 2, '8': 2, 'H': 2}, {'I': 0, 'x': 0, 'N': 1, 'd': 8, 'G': 5, 'H': 1}, {'1': 8, 'R': 1, 'r': 3, 'D': 6, 'L': 2, 'b': 4, '7': 4, 'q': 6, 'H': 1}, {'H': 2, 't': 9, 'p': 4, 'U': 9, '2': 2, 'P': 0, 'k': 4, 's': 0}]))

def computeFrequency(key, records):
    aDict = {}
    aList = getValuesForKey(key,records)
    for x in range(len(aList)):
        val = countMatchesByKey(key, aList[x], records)
        aDict[aList[x]] = val
    return aDict

print(computeFrequency("Artist", e))
print(computeFrequency("apples", [{'apples': 1, 'carrots': 7, 'bananas': 4, 'oranges': 2}, {'apples': 3, 'bananas': 3, 'oranges': 6}, {'apples': 4, 'carrots': 1, 'strawberries': 203, 'grapes': 2}, {'apples': 18, 'carrots': 10, 'bananas': 1, 'oranges': 9}, {'apples': 3, 'carrots': 0, 'bananas': 0, 'oranges': 0}]))
