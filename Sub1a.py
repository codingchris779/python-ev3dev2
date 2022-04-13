import imp
import math
from ClassStructure.Location import Location
robot = Location(6,-6,0)
startOfIsle = Location(6,30,90)
box = Location(15,30,90)
EndOfIsle = Location(102,30,90)
zoneB = Location(102,-6,180)
locs = [startOfIsle,box,EndOfIsle,zoneB]
for loc in locs:
    targetAng = math.degrees(math.atan(loc.getPos()[0]-robot.getPos()[0],loc.getPos()[1]-robot.getPos()[1]))