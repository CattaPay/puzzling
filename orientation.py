
# orientation of a piece
# contains width/height data 

class Orientation:
    def __init__(self, coords, height, width, char):
        self.coords = coords
        self.width = width
        self.height = height
        self.char = char
    
    def print(self):
        for i in range(self.height):
            outstr = ""
            for j in range(self.width):
                if (i,j) in self.coords:
                    outstr += self.char + " "
                else:
                    outstr += "O "
            print(outstr)
        print()
    
    def getCoords(self):
        return self.coords
    