#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-puzzle using hill-climbing.
# The tile board is represented as a 2D array with elements numbered according to the tile and the
# blank space has the value 0.

import numpy as np
from collections import deque

# Initial state (predefined)
init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Goal state (predefined)
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

# Search tree node structure.
class Node:
    def __init__(self, state):
        self.state = state
        self.h_cost = heuristic_cost(state)

    def heuristic_cost(state):
        return

# Print a tile pattern from given 'state'.
def print_pattern(state):
    for r in state:
        print('*******************')
        for c in r:
            print('| ', end=' ')
            if c != 0:
                print(f'{c}  ', end='')
            else:
                print(f'   ', end='')
        print('| ')
    print('*******************')

# Is there another tile on the same col., one row above?
def tile_above(state):
    (row, col) = np.where(state == 0)
    row = int(row)
    col = int(col)
    # top boundary
    return (None, None, None, None) if row == 0 else (row, col, row - 1, col)

# Is there another tile on the same col., one row below?
def tile_below(state):
    (row, col) = np.where(state == 0)
    row = int(row)
    col = int(col)
    # bottom boundary
    return (None, None, None, None) if row == (state.shape[0] - 1) else (row, col, row + 1, col)

# Is there another tile on the same row, one col. right?
def tile_right(state):
    (row, col) = np.where(state == 0)
    row = int(row)
    col = int(col)
    # right boundary
    return (None, None, None, None) if col == (state.shape[1] - 1) else (row, col, row, col + 1)

# Is there another tile on the same row, one col. left?
def tile_left(state):
    (row, col) = np.where(state == 0)
    row = int(row)
    col = int(col)
    # left boundary
    return (None, None, None, None) if col == 0 else (row, col, row, col - 1)

# Switch values of tiles (r1, c1) and (r2, c2) and return resulting state.
def switch_tiles(state, r1, c1, r2, c2):
    s = state.copy()
    temp = s[r2, c2]
    s[r2, c2] = 0
    s[r1, c1] = temp
    return s

# Returns lowest cost successor node for node of given state.
def lowest_cost_succesor(state):
    (r1, c1, r2, c2) = tile_above(state)
    if r1 != None:
        up_node = Node(switch_tiles(state, r1, c1, r2, c2))
    (r1, c1, r2, c2) = tile_below(state)
    if r1 != None:
        down_node = Node(switch_tiles(state, r1, c1, r2, c2))
    (r1, c1, r2, c2) = tile_right(state)
    if r1 != None:
        right_node = Node(switch_tiles(state, r1, c1, r2, c2))
    (r1, c1, r2, c2) = tile_left(state)
    if r1 != None:
        left_node = Node(switch_tiles(state, r1, c1, r2, c2))

def hill_climbing():
    current = Node(init_state)
    while True:
        #neighbor = #lowest_cost_successor
        print(neighbor.state)
        if neighbor.h_cost >= current.h_cost:
            return current.state
        current = neighbor
    return

print('Initial state:\n')
print_pattern(init_state)
#solution_state = hill_climbing()
#print_pattern(solution_state)
print("\n*** Solved ***")

# EOF.
