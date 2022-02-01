#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## main
##

from re import M
import sys

from IABrain import IABrain

def coucou():
    print("coucou")

def aurevoir():
    print("aurevoir")

def main():
    myIa = IABrain()
    for line in sys.stdin:
        line = line.rstrip("\n")
        try:
            myIa.processingData(line)
        except:
            print("command invalid:", sys.exc_info()[0])
        
    return 0

if __name__ == "__main__":
    main()