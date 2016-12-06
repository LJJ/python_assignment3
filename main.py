__author__ = 'lujiji'

import  Map
import  Action
import algorithm


map = Map.Map(100,100)
mapData = map.createMap()
map.saveMap()

initialX, initialY = Action.createIntialPoints(map)
pointX, pointY, sensorReading, alpha = Action.generateConsecutivePoints(initialX, initialY, map)

Action.saveTraj(initialX, initialY, pointX, pointY, sensorReading, alpha)


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
al.start(False)


# for i in result:
#     print(i)

# Map.mainloop()



