__author__ = 'lujiji'

import  Map
import  Action
map = Map.Map()
mapData = map.createMap()
map.saveMap()

initialX, initialY = Action.createIntialPoints(map)
Action.generateConsecutivePoints(initialX, initialY, map)

Map.mainloop()
