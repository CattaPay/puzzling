
from game import *
# TreeManager contains methods for finding solutions to the puzzle

class TreeManager:
    def __init__(self, board, pieces):
        self.board = board
        self.pieces = pieces
        self.layers = [] # 2d array of 
        self.piecesUsed = [] # piece used for each layer of the tree
        self.height = 0 # current height of the tree
        self.initializeRoot()

    def initializeRoot(self):
        root = Game(self.board, self.pieces)
        self.layers.append([root])
        return True
    
    def iterate(self, piece):
        if piece in self.piecesUsed:
            print("Can't use piece again")
            return False
        
        newLayer = []
        counter = 0
        for node in self.layers[self.height]:
            newLayer += node.playPiece(piece)
            counter += 1
            if counter % 50000 == 0:
                print(counter)
        
        self.layers.append(newLayer)
        self.height += 1
        self.piecesUsed.append(piece)
        return True
    
    def getLayers(self):
        layerLens = []
        for layer in self.layers:
            layerLens.append(len(layer))
        return layerLens

    def printLayers(self):
        for layer in range(self.height + 1):
            print(len(self.layers[layer]))
    
    def printLastLayer(self):
        print(len(self.layers[self.height]))
    
    def printSolutions(self):
        for node in self.layers[self.height]:
            print()
            node.printBoard()
    
    def getSolution(self):
        node = self.layers[self.height][0]
        val = node.returnBoard()
        return val


        
    

