#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## main
##

from re import M
import sys

from pisvorkProtocol import piskvorkProtocol

def main():
    myIa = piskvorkProtocol()
    for line in sys.stdin:
        line = line.rstrip("\n")
        if line == "END":
            break
        try:
            myIa.processingData(line)
        except:
            # print("command invalid:", sys.exc_info()[0])
            print("UNKNOWN", end="\r\n")
        
    return 0

if __name__ == "__main__":
    main()