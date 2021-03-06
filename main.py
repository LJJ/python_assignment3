__author__ = 'lujiji'

import  Map
import  Action
import algorithm
import matplotlib.pyplot as plt
import numpy as np
import math



# map = Map.Map(100,100)
# mapData = map.createMap()
# # map.saveMap()
# # mapData = map.readMap()
#
# initialX, initialY = Action.createIntialPoints(map)
# pointX, pointY, sensorReading, alpha = Action.generateConsecutivePoints(initialX, initialY, map, steps=100)
# Action.saveTraj(initialX, initialY, pointX, pointY, sensorReading, alpha)
# # initialX, initialY, pointX, pointY, sensorReading, alpha = Action.readTraj()
#
#
#
# # print(Action.readTraj())
#
#
#
# # mapData = [["H","H","T"],
# #        ["N","N","N"],
# #        ["N","B","H"]]
# # actions = [(0,1),(0,1),(1,0),(1,0)]
# # observation = ["N","N","H","H"]
#
# actions = [0 for i in range(100)]
# for i in range(len(alpha)):
#     if alpha[i] == 'R':
#         actions[i] = (0,1)
#     if alpha[i] == 'D':
#         actions[i] = (1,0)
#     if alpha[i] == 'L':
#         actions[i] = (0,-1)
#     if alpha[i] == 'U':
#         actions[i] = (-1,0)
#
# observation = sensorReading
#
# al = algorithm.Algorithm(mapData, actions, observation)
# proMap, maxResult = al.start(False)
# print( maxResult)
# print(pointX[-1], pointY[-1])
# # diff = abs(maxResult["location"][0]-pointY[-1]) + abs(maxResult["location"][1]-pointX[-1])
# # print(diff)
# # print(maxResult)
#
# # for i in proMap:
# #     print(i)
# map.drawHeatMap(proMap, maxResult)
# # heatmap = plt.pcolor(proMap)
# # Map.mainloop()
# # for y in range(len(proMap)):
# #     for x in range(len(proMap[y])):
# #         proMap[y][x] *= 100
# # colorMap = np.array(proMap)
# # plt.imshow(colorMap, cmap='hot')
# # plt.show()


def experiment():
    expResult = []

    for i in range(40):
        print(i)
        rowResult = []
        map = Map.Map(100,100)
        mapData = map.createMap()
        initialX, initialY = Action.createIntialPoints(map)
        pointX, pointY, sensorReading, alpha = Action.generateConsecutivePoints(initialX, initialY, map, steps=100)
        Action.saveTraj(initialX, initialY, pointX, pointY, sensorReading, alpha)
        actions = [0 for i in range(100)]
        for i in range(len(alpha)):
            if alpha[i] == 'R':
                actions[i] = (0,1)
            if alpha[i] == 'D':
                actions[i] = (1,0)
            if alpha[i] == 'L':
                actions[i] = (0,-1)
            if alpha[i] == 'U':
                actions[i] = (-1,0)
        observation = sensorReading
        al = algorithm.Algorithm(mapData, actions, observation)
        proMap, maxResult = al.start(True)
        for i in range(5,len(maxResult)):
            diff = abs(maxResult[i]["location"][0]-pointY[i]) + abs(maxResult[i]["location"][1]-pointX[i])
            rowResult.append(diff)
        expResult.append(rowResult)

    avarage_result = []
    for i in range(0,len(expResult[0])):
        total = 0.0
        for row in expResult:
            total += row[i]
        avarage_result.append(total/len(expResult))
    print(avarage_result)


experiment()

