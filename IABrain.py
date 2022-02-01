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

    iaName = "Randodo"
    version = "0.0.1"
    author = "4nton1n_l3_bo22"
    country = "FRANCE"

    map = []

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


    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart,
        "ABOUT": cmdAbout,
        "TURN": cmdTurn,
    }

    # def __init__(self):
    #     print("I'm alive !!")

    def processingData(self, cmd):
        list = re.findall(r"[\w']+", cmd)
        print(list)
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)
