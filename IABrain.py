#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

import random
import re


class IABrain:

    def computeSolution(self):
        size = len(self.map[0])
        rx = random.randint(0, size)
        ry = random.randint(0, size)

        self.map[rx][ry] = 1

        print("{}, {}".format(rx, ry))


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
            .format(self.iaName,
                    self.version,
                    self.author,
                    self.country))


    def cmdTurn(self, x, y):
        self.map[int(x)][int(y)] = 2
        self.computeSolution(self)
    
    def cmdBoard(self, list):
        for i in list:
            print()


    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart,
        "ABOUT": cmdAbout,
        "TURN": cmdTurn,
        "BOARD": cmdBoard,
    }

    def __init__(self):
        print("I'm alive !!")
        self.map = []
        self.iaName = "Randodo"
        self.version = "0.0.1"
        self.author = "4nton1n_l3_bo22"
        self.country = "FRANCE"

    def processingData(self, cmd):
        list = re.findall(r"[\w']+", cmd)
        print(list)
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)
