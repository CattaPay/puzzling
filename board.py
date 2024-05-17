
## board is a set of coordinates to include, (0,0) is top left
class Board:
    def __init__(self, height = 0, width = 0, coords = None):
        if coords != None:
            self.getFromCoords(coords)
            self.createPrintMap()
        else:
            self.coords = set()
            for i in range(height):
                for j in range(width):
                    self.coords.add((i,j))
            self.height = height
            self.width = width
            self.createPrintMap()
    
    def getDims(self):
        return self.height, self.width

    # could make this a set difference
    def removeCoords(self, toRemove):
        for coord in toRemove:
            self.coords.remove(coord)
    
    # could make this a set union
    def addCoords(self, toAdd):
        for coord in toAdd:
            self.coords.add(coord)
        self.updatePrintMap(toAdd, "O")


    def addBlockers(self, blockers):
        self.removeCoords(blockers)
        self.updatePrintMap(blockers, "X")

    # self.printMap is dictionary from (x,y) coords to character in that spot
    def createPrintMap(self):
        self.printMap = {}
        for i in range(self.height):
            for j in range(self.width):
                if (i,j) in self.coords:
                    self.printMap[(i,j)] = "O"
                else:
                    self.printMap[(i,j)] = "X"
    
    # updates self.printMap, should be called any time a change is made
    def updatePrintMap(self, coords, char):
        for coord in coords:
            self.printMap[coord] = char

    def getFromCoords(self, coords):
        self.coords = set(coords)
        self.height = 0
        self.width = 0
        for i,j in self.coords:
            if i > self.height:
                self.height = i
            if j > self.width:
                self.width = j
        self.height += 1
        self.width += 1


    def print(self, verbose = True):
        if verbose:
            print(str(self.height) + " x " + str(self.width) + " board")
        outstr = ""
        for i in range(self.height):
            for j in range(self.width):
                outstr += self.printMap[(i,j)] + " "
            outstr += "\n"
        if verbose:
            print(outstr)
        return outstr
    
    # places a piece in orientation with top left at (row,col)
    def placePiece(self, orientation, row, col):
        if self.height < row + orientation.height:
            return False
        if self.width < col + orientation.width:
            return False
        
        currentCoords = orientation.getCoords()
        adjCoords = self.getAdjustedCoords(currentCoords, row, col)

        # return false if it doesn't fit in the board
        if adjCoords != adjCoords.intersection(self.coords):
            return False
        
        # if it fits, place in board
        self.removeCoords(adjCoords)
        self.updatePrintMap(adjCoords, orientation.char)
        return True
    
    # same as placePiece but takes a tuple(orientation, row, col)
    def playMove(self, move):
        return self.placePiece(move[0], move[1], move[2])
    
    # same as removePiece but takes a tuple(orientation, row, col)
    def unplayMove(self, move):
        self.removePiece(move[0], move[1], move[2])
    
    def getAdjustedCoords(self, originalCoords, row, col):
        adjCoords = set()
        for x,y in originalCoords:
            adjCoords.add((x + row, y + col))
        return adjCoords

    # only call if there is a piece there
    def removePiece(self, orientation, row, col):
        adjCoords = self.getAdjustedCoords(orientation.getCoords(), row, col)
        self.addCoords(adjCoords)

    # returns a deep(ish) copy of board
    # gonna be too thicc
    def copy(self):
        newCoords = set()
        for i in self.coords:
            newCoords.append(i)



# board = Board(coords= [(0,0), (1,0), (2,0), (0,1), (2,1), (0,2), (1,2), (2,2)])

#bruh = set([[1,2], [3,4]])
#print(bruh)