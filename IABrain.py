#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## brainIA
##

from random import randint

class Brain:
    def __init__(self) -> None:
        print("MESSAGE I'm alive !!")
        self.iaName = "Randodo"
        self.version = "0.0.1"
        self.author = "4nton1n_l3_bo22"
        self.country = "FRANCE"
        self.map = []

    def computeSolution(self) -> None:
        print("tetw")
        size = len(self.map[0])
        print(size)
        
        rx = randint(0, size - 1)
        ry = randint(0, size - 1)

        self.map[rx][ry] = 1

        print("{}, {}".format(rx, ry))
    
    def show_map(self):
        for i in range(len(self.map)):
            for x in range(len(self.map[0])):
                print(self.map[i][x], " ", end="")
            print()