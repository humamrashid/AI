#!/usr/bin/python3

# Solution for 8-puzzle.

import numpy as np

# 8-puzzle is represented as a 1d array, initialized with default values representing the initial
# state (numbered tiles). A value of 0 indicates the blank tile.
puzzle = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Indicates current position of blank tile, initially (1, 2).
blank_pos = (1, 2)

def print_puzzle():
    for r in puzzle:
        print('*******************')
        for c in r:
            print('| ', end=' ')
            if c != 0:
                print(f'{c}  ', end='')
            else:
                print(f'   ', end='')
        print('| ')
    print('*******************')

# Same col., one row above.
def blank_above(pos):
    return True if pos[1] == blank_pos[1] and (pos[0] - blank_pos[0] == 1) else False

# Sample col., one row below.
def blank_below(pos):
    return True if pos[1] == blank_pos[1] and (blank_pos[0] - pos[0] == 1) else False

# Same row, one col. right.
def blank_right(pos):
    return True if pos[0] == blank_pos[0] and (blank_pos[1] - pos[1] == 1) else False

# Same row, one col. left
def blank_left(pos):
    return True if pos[0] == blank_pos[0] and (pos[1] - blank_pos[1] == 1) else False

print('Initial state:\n')

print_puzzle()

print(blank_right((1,1)))

print('\nSolved')

# EOF.
