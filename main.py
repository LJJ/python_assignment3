__author__ = 'lujiji'

import  Map
from Node import Location
# map = Map.Map()
# mapData = map.createMap()
# map.saveMap()
# Map.mainloop()


def calculate(location, action, most):
    preLoc = location.preLocation(action)
    obIndex = len(result)-1
    print(location)
    print(preLoc)
    p = result[-1][location.y][location.x]*observeP(location,observation[obIndex])*0.1
    if preLoc.x < 0 or preLoc.y <0 or preLoc is Location(1,2):
        return p
    else:
        if most is True:
            p = max(result[-1][preLoc.y][preLoc.x]*observeP(preLoc,observation[len(result)-1])*0.9, p)
        else:
            p += result[-1][preLoc.y][preLoc.x]*observeP(preLoc,observation[len(result)-1])*0.9
        return p


def observeP(loc, ob):
    if mapData[loc.y][loc.x] is ob:
        return 0.9
    else:
        return 0.05

def normalize(resultSlice):
    a = 1.0/(sum(resultSlice[0])+sum(resultSlice[1])+sum(resultSlice[2]))
    for y in range(len(resultSlice)):
        for x in range(len(resultSlice[y])):
            resultSlice[y][x] *= a
    return resultSlice

mapData = [["H","H","T"],
       ["N","N","N"],
       ["N","B","H"]]
actions = [(0,1),(0,1),(1,0),(1,0)]
observation = ["N","N","H","H"]
result = []

resultSlice = [[0.0 for i in range(3)] for j in range(3)]
for y in range(len(mapData)):
    for x in range(len(mapData[y])):
        if y == 2 and x == 1:
            continue
        resultSlice[y][x] = 1.0/8
result.append(resultSlice)


for i in range(0, len(actions)):
    resultSlice = [[0.0 for m in range(3)] for n in range(3)]
    for y in range(len(mapData)):
        for x in range(len(mapData[y])):
            if y == 2 and x == 1:
                continue
            location = Location(x,y)
            resultSlice[y][x] = calculate(location, actions[i], False)
    result.append(normalize(resultSlice))

for i in result:
    print(i)