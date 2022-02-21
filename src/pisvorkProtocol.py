#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## pisvorkProtocol
##

from code import interact
from distutils.log import INFO
import re
import sys
from IABrain import Brain

class piskvorkProtocol(Brain):

    def __init__(self):
        self.brain = Brain()

    def cmdBegin(self):
        self.brain.computeSolution(True);


    def cmdEnd(self):
        return


    def cmdStart(self, size):
        if int(size) > 20:
            print("ERROR too_big", end = "\r\n", flush = True)
            exit(84)
        if int(size) < 5:
            print("ERROR too_small", end = "\r\n", flush = True)
            exit(84)
        self.brain.size = int(size)
        print("OK", end = "\r\n", flush = True)


    def cmdAbout(self):
        print('name=\"{}\", version=\"{}\", author=\"{}\", country=\"{}\"'\
            .format(self.brain.iaName,
                    self.brain.version,
                    self.brain.author,
                    self.brain.country), end = "\r\n", flush = True)


    def cmdTurn(self, x : int, y : int):
        self.brain.putPiece(x, y, False)
        self.brain.computeSolution(False)
    
    def cmdBoard(self):
        for line in sys.stdin:
            line = line.rstrip("\n")
            if line == "DONE":
                break

            coor = re.findall(r"[\w']+", line)
            self.brain.putPiece(int(coor[0]), int(coor[1]), True if int(coor[2]) == 1 else False)
        self.brain.computeSolution(False)
    
    def cmdInfo(self, list) -> None:
        return None

    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart,
        "ABOUT": cmdAbout,
        "TURN": cmdTurn,
        "BOARD": cmdBoard,
        "INFO": cmdInfo
    }

    def processingData(self, cmd : str) -> None:
        list = re.findall(r"[\w']+", cmd)
        args = list[1:]
        args.insert(0, self)
        if list[0] == "INFO":
            return
        self.piskvorkCmd[list[0]](*args)