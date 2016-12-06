__author__ = 'lujiji'
from Node import Location

class Algorithm:

    def __init__(self, mapData, actions, observations):
        self.mapData = mapData
        self.actions = actions
        self.length = len(mapData)
        self.observations = observations
        self.result = []
        self.maxResult = []

    def start(self, isMax):
        resultSlice = [[0.0 for i in range(self.length)] for j in range(self.length)]
        for y in range(self.length):
            for x in range(len(self.mapData[y])):
                if self.mapData[y][x] is "B":
                    continue
                resultSlice[y][x] = 1.0/(self.length*self.length*0.8)
        self.result.append(resultSlice)

        for i in range(0, len(self.actions)):
            maxP = 0
            maxLoc = None
            resultSlice = [[0.0 for m in range(self.length)] for n in range(self.length)]
            for y in range(self.length):
                for x in range(len(self.mapData[y])):
                    if self.mapData[y][x] is "B":
                        continue
                    location = Location(x,y)
                    p = self.calculate(location, self.actions[i], isMax)
                    resultSlice[y][x] = p
                    if p>maxP:
                        maxP = p
                        maxLoc = (location.y,location.x)
            nor_data, a = self.normalize(resultSlice)
            self.result.append(nor_data)
            self.maxResult.append({"location":maxLoc,"p":maxP*a})
        # print(len(self.result), len(self.maxResult))
        return self.result[-1], self.maxResult


    def isValid(self, location):
        if location.x < self.length and location.y<self.length and location.x>=0 and location.y>=0:
            if self.mapData[location.y][location.x] is not "B":
                return True
        return False

    def calculate(self, location, action, most):
        preLoc = location.preLocation(action)
        nextLoc = location.nextLocation(action)
        obIndex = len(self.result)-1

        p = self.result[-1][location.y][location.x]*self.observeP(location,self.observations[obIndex])
        if self.isValid(nextLoc) is True:
                p *= 0.1
        if self.isValid(preLoc) is False:
            return p
        else:
            if most is True:
                p = max(self.result[-1][preLoc.y][preLoc.x]*self.observeP(location,self.observations[len(self.result)-1])*0.9, p)
            else:
                p += self.result[-1][preLoc.y][preLoc.x]*self.observeP(location,self.observations[len(self.result)-1])*0.9
            return p


    def observeP(self,loc, ob):
        if self.mapData[loc.y][loc.x] is ob:
            return 0.9
        else:
            return 0.05

    def normalize(self,resultSlice):
        total = 0.0
        for row in resultSlice:
            total += sum(row)
        a = 1.0/total
        for y in range(len(resultSlice)):
            for x in range(len(resultSlice[y])):
                resultSlice[y][x] *= a
        return resultSlice, a
