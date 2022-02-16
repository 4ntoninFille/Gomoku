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
import sys

class Brain:
    def __init__(self) -> None:
        self.iaName = "Randodo"
        self.version = "0.0.1"
        self.author = "4nton1n_l3_bo22"
        self.country = "FRANCE"
        self.map = []
        self.size = 0

    def putPiece(self, x, y, v):
        index : int = x * y

    def computeSolution(self, begin : bool) -> None:
        size = len(self.map[0])

        rx : int = randint(0, size - 1)
        ry : int = randint(0, size - 1)

        if begin == True:
            rx = ry = round(size / 2)

        self.map[rx][ry] = 1

        print("{},{}".format(rx, ry), end = "\r\n")

    def minimax(self, newMap, turn : int, depth : int) -> int:
        if depth <= 0:
            return 0
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