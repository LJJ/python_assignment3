__author__ = 'Siyu Chen'

from Tkinter import *
import random
import Map

# map = Map.Map()
def createIntialPoints(Map):
    initialX = random.randrange(0, 100)
    initialY = random.randrange(0, 100)
    while Map.mapData[initialY][initialX] == "B":
        initialX = random.randrange(0, 100)
        initialY = random.randrange(0, 100)
    print initialX, initialY
    return initialX, initialY

def generateConsecutivePoints(initialX, initialY, Map, steps):
    currentX = initialX
    currentY = initialY
    alpha = [None for i in range(steps)]
    sensorReading = [None for i in range(steps)]

    Idx = 0
    pointX = [0 for i in range(steps + 1)]
    pointY = [0 for i in range(steps + 1)]
    pointX[0] = initialX
    pointY[0] = initialY
    for i in range(0, steps):
        transition= random.randrange(0, 10)
        if transition == 0:
            currentX = pointX[i]
            currentY = pointY[i]
            direction = random.randrange(0, 4)
            if direction == 0:
                alpha[i] = 'U'
            elif direction == 1:
                alpha[i] = 'L'
            elif direction == 2:
                alpha[i] = 'D'
            elif direction == 3:
                alpha[i] = 'R'
        else:
            direction = random.randrange(0, 4)
            if direction == 0:
                alpha[i] = 'U'
                currentY = pointY[i] + 1
                if currentY > 99 or Map.mapData[currentY][currentX] == "B":
                    currentY = pointY[i]
            elif direction == 1:
                alpha[i] = 'L'
                currentX = pointX[i] - 1
                if currentX < 0 or Map.mapData[currentY][currentX] == "B":
                    currentX = pointX[i]
            elif direction == 2:
                alpha[i] = 'D'
                currentY = pointY[i] - 1
                if currentY < 0 or Map.mapData[currentY][currentX] == "B":
                    currentY = pointY[i]
            elif direction == 3:
                alpha[i] = 'R'
                currentX = pointX[i] + 1
                if currentX > 99 or Map.mapData[currentY][currentX] == "B":
                    currentX = pointX[i]

        # print 'aaa',alpha[i]
        observation = random.randrange(0, 10)
        if observation == 0:
            cells = ['N', 'H', 'T']
            sensorIdx = cells.index(Map.mapData[currentY][currentX])
            cells.pop(sensorIdx)
            sensorOther = random.randrange(0, 1)
            newChar = cells[sensorOther]
        else:
            newChar = Map.mapData[currentY][currentX]
        pointX[i+1] = currentX
        pointY[i+1] = currentY
        sensorReading[i] = newChar
        # print currentX, currentY
        # print newChar
    return pointX, pointY, sensorReading, alpha

def saveTraj(initialX, initialY, pointX, pointY, sensorReading, alpha):
    f = open("./path.txt","w")
    f.write("%d,%d" % (initialX, initialY))
    # print len(pointX), len(pointY), len(sensorReading), len(alpha)
    for i in range(0,len(sensorReading)):
        line = "%s,%s,%s,%s" % (pointX[i+1], pointY[i+1], alpha[i], sensorReading[i])
        f.write("\n"+line)
    f.close()


def readTraj():
    content = open("./path.txt").read().split("\n")
    row1 = content.pop(0)
    initX = int(row1.split(",")[0])
    initY = int(row1.split(",")[1])
    xArray = []
    yArray = []
    sensor = []
    actions = []
    for line in content:
        component = line.split(",")
        xArray.append(int(component[0]))
        yArray.append(int(component[1]))
        sensor.append(component[3])
        actions.append(component[2])
    return initX, initY, xArray, yArray, sensor, actions




