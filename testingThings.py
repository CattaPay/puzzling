from piece import *
from board import *
from game import *
from treeManager import *
from treeOptimizer import *
board = Board(4,4)
board.addBlockers([(2,1)])
board.addBlockers([(0,0)])
print()
print()
#board.print()
t_piece = Piece([(0,0), (0,1), (0,2), (1,1), (1,2)], char = "T")
long_piece = Piece([(0,0), (0,1), (0,2), (0,3)], char = "L")
hook_piece = Piece([(0,0), (0,1), (0,2), (1,0)], char = "H")

# game = Game(board, [t_piece, long_piece, hook_piece])

# nodes = game.playPiece(hook_piece)

# # for node in nodes:
# #     node.printBoard()
# nextLayer = []
# for node in nodes:
#     nextLayer += node.playPiece(t_piece)

# lastLayer = []
# for node in nextLayer:
#     lastLayer += node.playPiece(long_piece)

# for node in lastLayer:
#     node.printBoard()

# print(len(lastLayer))

biggerBoard = Board(5, 5)
biggerBoard.addBlockers([(4,2), (4,3), (4,4), (0,0)])
# biggerBoard.print()

fullBoard = Board(7,7)
fullBoard.addBlockers([(6,3), (6,4), (6,5), (6,6), (0,6), (1,6)])
# fullBoard.addBlockers([(0,5), (6,0)])
fullBoard.print()

z_piece = Piece([(0,0), (0,1), (1,1), (2,1), (2,2)], "Z")
nice_piece = Piece([(0,0), (0,1), (0,2), (1,1), (1,2)], "N")
l_piece = Piece([(0,0), (0,1), (0,2), (0,3), (1,3)], "L")
u_piece = Piece([(0,0), (0,1), (0,2), (1,0), (1,2)], "U")
square_piece = Piece([(0,0), (0,1), (0,2), (1,0), (1,1), (1,2)], "G")
t_piece = Piece([(0,0), (0,1), (0,2), (0,3), (1,1)], "T")
angle_piece = Piece([(0,0), (0,1), (0,2), (1,0), (2,0)], "B")
squiggle_piece = Piece([(0,0), (0,1), (0,2), (1,2), (1,3)], "S")

allPieces = [z_piece, nice_piece, l_piece, u_piece, square_piece, t_piece, angle_piece, squiggle_piece]

# a = TreeOptimizer(fullBoard, allPieces, 9, 11)
# a.blockDates()
# print(a.optimizeAndRun(3, True))

# runData = {}
# for m in range(5,7):
#     for i in range(1,32):
#         month = m
#         day = i
#         if not (month == 5 and day <= 6): 
#             a = TreeOptimizer(fullBoard, allPieces, month, day)
#             a.blockDates()
#             data = a.optimizeAndRun(3, True)
#             runData[(month,day)] = data
#             a.unblockDates()
#             f = open("data.txt", "a")
#             f.write(str(month) + "," + str(day) + "," + str(data[1]) + "," + str(data[2]) + "," + str(data[3]) + "," + str(data[4]) + "\n" + str(data[5]) + "\n")
#             f.close()

# print(runData)
tree = TreeManager(fullBoard, allPieces)
tree.iterate(allPieces[4])
tree.iterate(allPieces[6])
tree.iterate(allPieces[0])
tree.printLayers()

# tree = TreeManager(fullBoard, allPieces)
# tree.iterate(allPieces[4])
# tree.iterate(allPieces[6])
# tree.iterate(allPieces[0])
# tree.iterate(allPieces[3])
# tree.printLayers()
# tree.iterate(allPieces[2])
# tree.printLayers()
# tree.iterate(allPieces[7])
# tree.printLayers()
# tree.iterate(allPieces[5])
# tree.printLayers()
# tree.iterate(allPieces[1])

# tree.iterate(allPieces[4])
# tree.iterate(allPieces[0])
# tree.iterate(allPieces[6])
# tree.iterate(allPieces[1])
# tree.printLayers()

# tree.iterate(allPieces[3])
# tree.printLayers()
# tree.iterate(allPieces[5])
# tree.printLayers()
# tree.iterate(allPieces[2])
# tree.printLayers()
# tree.iterate(allPieces[7])
# tree.printLayers()



# tree.iterate(allPieces[4])
# tree.iterate(allPieces[0])
# tree.iterate(allPieces[7])
# tree.iterate(allPieces[3])
# tree.iterate(allPieces[1])
# tree.printLayers()
# tree.iterate(allPieces[2])
# tree.printLayers()
# tree.iterate(allPieces[5])
# tree.printLayers()
# tree.iterate(allPieces[6])



# tree.iterate(allPieces[1])
# tree.printLayers()

# tree.iterate(allPieces[3])
# tree.printLayers()



# tree.iterate(u_piece)
# tree.iterate(nice_piece)
# tree.iterate(l_piece)
# tree.iterate(long_piece)
# tree.iterate(hook_piece)

# tree.printLayers()
# tree.printSolutions()
