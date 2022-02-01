#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## pisvorkProtocol
##

import re
import sys
from IABrain import Brain

class piskvorkProtocol(Brain):

    def __init__(self):
        self.brain = Brain()

    def cmdBegin(self):
        self.brain.computeSolution();


    def cmdEnd(self):
        print("end")


    def cmdStart(self, size):
        print("OK - everything is good")
        self.brain.map = [[0 for _ in range(int(size))] for _ in range(int(size))]


    def cmdAbout(self):
        print('name=\"{}\", version=\"{}\", author=\"{}\", country=\"{}\"'\
            .format(self.brain.iaName,
                    self.brain.version,
                    self.brain.author,
                    self.brain.country))


    def cmdTurn(self, x, y):
        print(x, y)
        self.brain.map[int(x)][int(y)] = 2
        self.brain.computeSolution()
    
    def cmdBoard(self):
        for line in sys.stdin:
            line = line.rstrip("\n")
            if line == "DONE":
                break

            coor = re.findall(r"[\w']+", line)
            self.brain.map[int(coor[0])][int(coor[1])] = int(coor[2])
        self.brain.computeSolution()


    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart,
        "ABOUT": cmdAbout,
        "TURN": cmdTurn,
        "BOARD": cmdBoard,
    }

    def processingData(self, cmd : str) -> None:
        list = re.findall(r"[\w']+", cmd)
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)