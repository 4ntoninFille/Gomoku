#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

from ast import arg
from tokenize import String


class IABrain:

    map = []

    def cmdBegin(self):
        print ("begin")

    def cmdEnd(self):
        print("end")

    def cmdStart(self, size):
        print("OK - everything is good")
        self.map = [[0] * int(size)] * int(size)
        for i in self.map:
            print(i)


    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart
    }

    def __init__(self):
        print('i m alive !!')

    def processingData(self, cmd):
        list = cmd.split()
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)
