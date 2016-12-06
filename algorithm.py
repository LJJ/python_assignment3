__author__ = 'lujiji'
from Node import Location

class Algorithm:

    def __init__(self, mapData, actions, observations):
        self.mapData = mapData
        self.actions = actions
        self.observations = observations
        self.result = []


    def start(self, isMax):
        resultSlice = [[0.0 for i in range(3)] for j in range(3)]
        for y in range(len(self.mapData)):
            for x in range(len(self.mapData[y])):
                if y == 2 and x == 1:
                    continue
                resultSlice[y][x] = 1.0/8
        self.result.append(resultSlice)


        for i in range(0, len(self.actions)):
            resultSlice = [[0.0 for m in range(3)] for n in range(3)]
            for y in range(len(self.mapData)):
                for x in range(len(self.mapData[y])):
                    if y == 2 and x == 1:
                        continue
                    location = Location(x,y)
                    resultSlice[y][x] = self.calculate(location, self.actions[i], isMax)
            # print(resultSlice)
            self.result.append(self.normalize(resultSlice))
            print(self.result[-1])

    def calculate(self, location, action, most):
        preLoc = location.preLocation(action)
        nextLoc = location.nextLocation(action)
        obIndex = len(self.result)-1

        p = self.result[-1][location.y][location.x]*self.observeP(location,self.observations[obIndex])
        if nextLoc.x <= 2 and nextLoc.y<=2:
            if nextLoc.x != 1 or nextLoc.y != 2:
                p *= 0.1
        if preLoc.x < 0 or preLoc.y < 0:
            return p
        if preLoc.x == 1 and preLoc.y == 2:
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
        a = 1.0/(sum(resultSlice[0])+sum(resultSlice[1])+sum(resultSlice[2]))
        for y in range(len(resultSlice)):
            for x in range(len(resultSlice[y])):
                resultSlice[y][x] *= a
        return resultSlice
