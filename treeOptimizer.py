
# handles optimizing the order of pieces placed
# also gives overhead for the running the search based on day
from treeManager import *
import time

class TreeOptimizer:
    def __init__(self, baseBoard, pieces, month, day):
        self.board = baseBoard
        self.pieces = pieces
        self.month = month
        self.day = day
        self.dayBlock = (((self.day-1) // 7) + 2, ((self.day-1) % 7))
        self.monthBlock = ((self.month-1) // 6, ((self.month-1) % 6))
    
    def blockDates(self):
        self.board.addBlockers([self.dayBlock, self.monthBlock])

    def unblockDates(self):
        self.board.addCoords([self.dayBlock, self.monthBlock])

    def multiIterate(self, tree, indices, verbose = False):
        for i in indices:
            tree.iterate(self.pieces[i])
            if verbose:
                tree.printLastLayer()
                print()



    def optimize(self, cutoffDepth):
        bestOrder = []
        remaining = list(range(len(self.pieces)))
        for depth in range(cutoffDepth):
            scores = {}
            for i in remaining:
                bestOrder.append(i)
                testTree = TreeManager(self.board, self.pieces)
                self.multiIterate(testTree, bestOrder)
                scores[i] = testTree.getLayers()[depth+1]
                bestOrder.remove(i)

            best = min(scores, key = lambda x: scores[x])
            # print(scores)
            scores.pop(best)
            bestOrder.append(best)
            remaining.remove(best)
            # print(bestOrder)
        while len(scores) > 0:
            best = min(scores, key = lambda x: scores[x])
            bestOrder.append(best)
            scores.pop(best)
        
        # print(bestOrder)
        return bestOrder
    
    def runTree(self, order, verbose = False):
        tree = TreeManager(self.board, self.pieces)
        self.multiIterate(tree, order, verbose)
        # if verbose:
        #     tree.printSolutions()
        return tree

    def optimizeAndRun(self, depthCutoff, verbose = False):
        if verbose:
            self.board.print()
        t1 = time.perf_counter()
        bestOrder = self.optimize(depthCutoff)
        t2 = time.perf_counter()
        if verbose:
            print("Best order is: ", bestOrder)
        
        t3 = time.perf_counter()
        tree = self.runTree(bestOrder, verbose)
        t4 = time.perf_counter()

        if verbose:
            tree.printLayers()
        # return tree, solutions, nodes visited, opt timer, run timer, printout
        return (tree, tree.getLayers()[len(tree.getLayers())-1], sum(tree.getLayers()), t2-t1, t4-t3, tree.getSolution())
