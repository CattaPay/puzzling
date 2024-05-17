
# contains a board and pieces to play
# can treat it as a node of a search tree
class Game:
    # board is a Board object
    # pieces is an array of Piece objects
    # moveList is an array of moves
    def __init__(self, board, pieces = None, allPieces = None, moveList = None):
        self.board = board

        self.pieces = [] # pieces that are available
        if pieces != None:
            for piece in pieces: # deep copy
                self.pieces.append(piece)
        
        self.allPieces = [] # all pieces
        if allPieces == None:
            for piece in self.pieces:
                self.allPieces.append(piece)
        else:
            if allPieces != None:
                for piece in allPieces:
                    self.allPieces.append(piece) 

        self.moveList = [] # list of moves to get here
        if moveList != None:
            for move in moveList:
                self.moveList.append(move)

        self.height, self.width = self.board.getDims()
    
    def addMove(self, move):
        self.moveList.append(move)
    
    def removePiece(self, piece):
        self.pieces.remove(piece)
    
    def createChild(self, move, playedPiece):
        newGame = Game(self.board, self.pieces, self.allPieces, self.moveList)
        # newGame.moveList = []
        # for preMove in self.moveList:
        #     newGame.moveList.append(preMove)
        newGame.addMove(move)
        newGame.removePiece(playedPiece)
        return newGame

    def playPiece(self, piece):
        self.makeMoves()
        # self.board.print()
        newNodes = []
        # can maybe put orientation at front and cut down on row/col checks
        for row in range(self.height):
            for col in range(self.width):
                for orientation in piece.getOrientations():
                    move = (orientation, row, col)
                    if self.board.playMove(move):

                        newNodes.append(self.createChild(move, piece))
                        self.board.unplayMove(move)
                        
        self.unmakeMoves()
        return newNodes

    def makeMoves(self):
        for move in self.moveList:
            self.board.playMove(move)
        
    def unmakeMoves(self):
        for move in self.moveList:
            self.board.unplayMove(move)
        
    def printBoard(self):
        self.makeMoves()
        val = self.board.print()
        self.unmakeMoves()
        return val
    
    def returnBoard(self):
        self.makeMoves()
        val = self.board.print(verbose = False)
        self.unmakeMoves()
        return val

