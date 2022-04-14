

import math


class Location: 
    pos = [0,0,0]
    def __init__(self, X = 0, Y=0, Rot=0) -> None:
        self.pos = [X,Y,Rot]
    def setPos(self,X,Y,Rot):
        self.pos = [X,Y,Rot%360]
    def getPos(self):
        return self.pos
    def translateLocal(self, fw, right, cw):
        self.pos[2]=cw
        self.pos[0]+= fw*math.cos(math.radians(self.pos[2]))+right*math.cos(math.radians(self.pos[2]-90))
        self.pos[1]+= fw*math.sin(math.radians(self.pos[2]))+right*math.sin(math.radians(self.pos[2]-90))



    
        