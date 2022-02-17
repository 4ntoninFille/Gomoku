#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

# x = 0 # empty
# x |= 1<<19 # set bit 19
# x &= ~(1<<19) # clear bit 19
# x ^= 1<<19 # toggle bit 19
# x = ~x # invert *all* bits, all the way to infinity
# mask = ((1<<20)-1) # define a 20 bit wide mask
# x &= mask # ensure bits 20 and higher are 0
# x ^= mask # invert only bits 0 through 19

# (x >> 19) & 1 # test bit 19
# (x >> 16) & 0xf # get bits 16 through 20.

from hashlib import new
from random import randint
import math
import sys

class Brain:
    def __init__(self) -> None:
        self.iaName = "Randodo"
        self.version = "0.0.1"
        self.author = "4nton1n_l3_bo22"
        self.country = "FRANCE"
        self.map = []
        self.size : int = 0

        self.mapAllies = 0
        self.mapEnemy = 0
        self.mapFree : int = 0

    #### Bits Function ####

    def putPiece(self, x : int, y : int, allies : bool) -> None:
        d = int(y) * self.size + int(x)
        self.mapFree |= 1 << int(d)

        if allies == True:
            self.mapAllies |= (1 << int(d))
        else:
            self.mapEnemy |= (1 << int(d))

    def setBitPiece(self, bits, index : int, value : int) -> int:
        if value == 0:
            bits &= ~(1<<int(index))
        else:
            bits |= (1 << int(index))
        return bits

    #######################

    def computeSolution(self, begin : bool) -> None:

        rx : int = randint(0, self.size - 1)
        ry : int = randint(0, self.size - 1)

        if begin == True:
            rx = ry = round(self.size / 2)
        else:
            index = self.minimax(0, self.mapFree, self.mapAllies, self.mapEnemy, True, 1, True)

            ry = math.floor(index / self.size)
            rx = index - self.size * ry


        # self.map[rx][ry] = 1

        self.putPiece(rx, ry, True)
        # print(bin(self.mapFree))
        print("{},{}".format(rx, ry), end = "\r\n")

    ## EVALUATION ##

    def evaluation(self, pos : int, mapFree, mapAllies, mapEnemy) -> int:
        valueEvaluation = 0
        if int(pos) - 1 >= 0 and (int(mapAllies) >> int(pos) - 1) & 1:
            valueEvaluation += 15
        else:
            valueEvaluation -= 15

        if int(pos) + 1 < int(self.size * self.size) and (int(mapAllies) >> int(pos) + 1) & 1:
            valueEvaluation += 15
        else:
            valueEvaluation -= 15
        if int(pos) - int(self.size) >= 0 and (int(mapAllies) >> int(pos) - int(self.size)) & 1:
            valueEvaluation += 15
        else:
            valueEvaluation -= 15
        if int(pos) - int(self.size) >= int(self.size * self.size) and (int(mapAllies) >> int(pos) - int(self.size)) & 1:
            valueEvaluation += 15
        else:
            valueEvaluation -= 15

        if int(pos) - 1 >= 0 and (int(mapEnemy) >> int(pos) - 1) & 1:
            valueEvaluation += 10
        else:
            valueEvaluation -= 10
        if int(pos) + 1 < int(self.size * self.size) and (int(mapEnemy) >> int(pos) + 1) & 1:
            valueEvaluation += 10
        else:
            valueEvaluation -= 10
        if int(pos) - int(self.size) >= 0 and (int(mapEnemy) >> int(pos) - int(self.size)) & 1:
            valueEvaluation += 10
        else:
            valueEvaluation -= 10
        if int(pos) - int(self.size) >= int(self.size * self.size) and (int(mapEnemy) >> int(pos) - int(self.size)) & 1:
            valueEvaluation += 10
        else:
            valueEvaluation -= 10    
        
        # print("eval=", valueEvaluation)
        return valueEvaluation

    ################

    def minimax(self, pos : int, mapFree, mapAllies, mapEnemy, allies : bool, depth : int, first : bool) -> int:
        if depth <= 0:
            return self.evaluation(pos, mapFree, mapAllies, mapEnemy)

        if allies:
            maxEval = -100000
            tmpMax = -100000
            bestIndex = 0
            for index in range(self.size * self.size):
                if ((int(mapFree) >> int(index)) & 1) == 0:
                    mapFree = self.setBitPiece(mapFree, index, 1)
                    mapAllies = self.setBitPiece(mapAllies, index, 1)

                    eval = self.minimax(index, mapFree, mapAllies, mapEnemy, False, depth - 1, False)
                    maxEval = max(maxEval, eval)

                    mapFree = self.setBitPiece(mapFree, index, 0)
                    mapAllies = self.setBitPiece(mapAllies, index, 0)
                    if tmpMax != maxEval:
                        bestIndex = index
                        tmpMax = maxEval
                    # if first:
                    #     return bestIndex
                    # else:
            if first:
                return bestIndex
            else:
                return maxEval
        else:
            minEval = 100000
            for index in range (self.size * self.size):
                if ((int(mapFree) >> int(index)) & 1) == 0:
                    mapFree = self.setBitPiece(mapFree, index, 1)
                    mapEnemy = self.setBitPiece(mapEnemy, index, 1)

                    eval = self.minimax(index, mapFree, mapAllies, mapEnemy, True, depth - 1, True)
                    minEval = min(minEval, eval)

                    mapFree = self.setBitPiece(mapFree, index, 0)
                    mapEnemy = self.setBitPiece(mapEnemy, index, 0)
            return minEval

        # for index in range(self.size * self.size):
        #     if (mapFree >> index) & 0:
        #         print()

            # evaluate position        
        # for x in range(len(newMap)):
        #     for y in range(len(newMap[0])):
        #         if newMap[x][y] == 0:
        #             if turn == 1:
        #                 newMap[x][y] = 1
        #             else:
        #                 newMap[x][y] = 2
        #         if depth <= 0:
        #             return
        #         self.newBoardRec(newMap, turn * -1, depth - 1)

        return 1

    
    def show_map(self):
        for i in range(len(self.map)):
            for x in range(len(self.map[0])):
                print(self.map[i][x], " ", end="")
            print()