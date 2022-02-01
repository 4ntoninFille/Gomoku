#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

from random import random

class Brain:
    def __init__(self) -> None:
        self.iaName = "Randodo"
        self.version = "0.0.1"
        self.author = "4nton1n_l3_bo22"
        self.country = "FRANCE"
        self.map = []

    def computeSolution(self) -> None:
        size = len(self.map[0])
        rx = random.randint(0, size)
        ry = random.randint(0, size)

        self.map[rx][ry] = 1

        print("{}, {}".format(rx, ry))