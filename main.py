__author__ = 'lujiji'

import  Map
import  Action
import algorithm
from Node import Location

map = Map.Map(100,100)
mapData = map.createMap()
map.saveMap()

steps = 100

initialX, initialY = Action.createIntialPoints(map)
pointX, pointY, sensorReading, alpha = Action.generateConsecutivePoints(initialX, initialY, map, steps)

Action.saveTraj(initialX, initialY, pointX, pointY, sensorReading, alpha)

# class path_id(Location):
#     def __init__(self,x,y):
#         self.x = x
#         self.y = y
#
# for i in range(len(pointX)):
#     path_id.append = pointX[i], pointY[i]
#
# for i in range(len(pointX)):
#     map.DrawLines(path_id[i], path_id)
#
# Map.mainloop()

# mapData = [["H","H","T"],
#        ["N","N","N"],
#        ["N","B","H"]]
# actions = [(0,1),(0,1),(1,0),(1,0)]
# observation = ["N","N","H","H"]

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
proMap = al.start(False)


# for i in result:
#     print(i)
# map.drawHeatMap(proMap)
# Map.mainloop()



