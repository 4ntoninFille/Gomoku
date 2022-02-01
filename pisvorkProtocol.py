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
        print("I'm alive !!")
        self.brain = Brain()
        self.map = []

    def cmdBegin(self):
        self.computeSolution();


    def cmdEnd(self):
        print("end")


    def cmdStart(self, size):
        print("OK - everything is good")
        self.map = [[0] * int(size)] * int(size)
        for i in self.map:
            print(i)


    def cmdAbout(self):
        print('name=\"{}\", version=\"{}\", author=\"{}\", country=\"{}\"'\
            .format(self.brain.iaName,
                    self.brain.version,
                    self.brain.author,
                    self.brain.country))


    def cmdTurn(self, x, y):
        self.map[int(x)][int(y)] = 2
        self.computeSolution(self)
    
    def cmdBoard(self):
        for line in sys.stdin:
            line = line.rstrip("\n")
            coor = re.findall(r"[\w']+", line)

            self.map[coor[0]][coor[1]] = coor[2]

            if line == "DONE":
                break

        self.computeSolution()


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
        print(list)
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)