#!/usr/bin/python3

# Solution for 8-puzzle.

import numpy as np

# 8-puzzle is represented as a 1d array, initialized with default values representing the initial
# state (numbered tiles). A value of 0 indicates the blank tile.
puzzle = np.array([(1,4,3), (7,8,0), (6,2,5)])

def print_puzzle():
    for r in puzzle:
        print('*******************')
        for c in r:
            print('| ', end=" ")
            print(f'{c}  ', end="")
            #print(' |', end="")
        print('| ')
    print('*******************')

print_puzzle()

# EOF.
