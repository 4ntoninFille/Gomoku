#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

from ast import arg
from inspect import _void
from tokenize import String


class IABrain:

    iaName = "Randodo"
    version = "0.0.1"
    author = "4nton1n_l3_bo22"
    country = "FRANCE"

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

    def cmdAbout(self):
        print('name=\"{}\", version=\"{}\", author=\"{}\", country=\"{}\"'.format(self.iaName,
                                                                                    self.version,
                                                                                    self.author,
                                                                                    self.country))


    piskvorkCmd = {
        "BEGIN": cmdBegin,
        "END": cmdEnd,
        "START": cmdStart,
        "ABOUT": cmdAbout,
    }

    # def __init__(self):
    #     print("I'm alive !!")

    def processingData(self, cmd):
        list = cmd.split()
        args = list[1:]
        args.insert(0, self)
        self.piskvorkCmd[list[0]](*args)
