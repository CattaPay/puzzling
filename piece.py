
from orientation import *
# piece is an array of coordinates
# contains the coordinates for the eight rotations in self.orientations
# char is the character rep for the piece

class Piece:
    def __init__(self, coords, char = None):
        self.coords = set(coords)
        self.orientations = []
        self.uniqueOrientations = 0
        self.height, self.width = self.getDims(self.coords)
        self.dims = max(self.height, self.width)
        if char:
            self.char = char
        else:
            self.char = "X"
        self.createOrientations()

    def getDims(self, coords):
        height = 0
        width = 0
        for i,j in coords:
            if i > height:
                height = i
            if j > width:
                width = j
        height = height + 1
        width = width + 1
        return (height, width)

    def rotate(self, coords):
        newCoords = set()
        newx = []
        newy = []
        min_x = min_y = 10000
        for x,y in coords:
            newx.append(-y)
            if -y < min_x:
                min_x = -y
            newy.append(x)
            if x < min_y:
                min_y = x

        for i,j in zip(newx, newy):
            newCoords.add((i-min_x, j-min_y))
        return newCoords

    # code is scuffed but should only run once so it's fine?
    def createOrientations(self):
        allOrientations = [0] * 8
        allOrientations[0] = self.coords
        for i in range(3):
            allOrientations[i+1] = self.rotate(allOrientations[i])
        for i in range(4):
            allOrientations[i+4] = self.flip(allOrientations[i])
        
        coordlist = []
        for i in range(8):
            if not allOrientations[i] in coordlist:
                coordlist.append(allOrientations[i])
        
        for i in range(len(coordlist)):
            height, width = self.getDims(coordlist[i])
            self.orientations.append(Orientation(coordlist[i], height, width, self.char))
    
    def getOrientation(self, n):
        if n >= len(self.orientations):
            print("Orientation doesn't exist")
            return False
        return self.orientations[n]

    def getOrientations(self):
        return self.orientations
        
    def flip(self, coords):
        newCoords = set()
        newx = []
        newy = []
        min_x = 10000
        for x,y in coords:
            newx.append(-x)
            if -x < min_x:
                min_x = -x
            newy.append(y)
        
        for i,j in zip(newx, newy):
            newCoords.add((i-min_x, j))
        return newCoords
    
    def printOrientations(self):
        print()
        for rot in range(len(self.orientations)):
            print("Orientation " + str(rot + 1) + ": ")
            self.orientations[rot].print()
            print()

    # def __eq__(self, value):
    #     return self.coords == value.coords
    


