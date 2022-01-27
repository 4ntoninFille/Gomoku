#!/usr/bin/env python3
##
## EPITECH PROJECT, 2022
## B-AIA-500-NCE-5-1-gomoku-antonin.fille
## File description:
## main
##

import sys

def coucou():
    print("coucou")

def aurevoir():
    print("aurevoir")

piskvorkCmd = {
    "1\n": coucou,
    "2\n": aurevoir,
}

def main():
    for line in sys.stdin:
        try:
            piskvorkCmd[line]()
        except:
            print("command invalid")
        
    return 0

if __name__ == "__main__":
    main()