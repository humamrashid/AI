#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-puzzle using hill-climbing; heuristic used is 'Manhattan distance.'
# The tile board is represented as a 2D array with elements numbered according to the tile and the
# blank space has the value 0.

import numpy as np
import random

# Initial state (predefined)
init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Goal state (predefined)
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

# Search tree node structure.
class Node:
    def __init__(self, state):
        self.state = state
        self.h_cost = self.heuristic_cost()
    def heuristic_cost(self):
        distances = []
        for i in range(0, 9):
            (r, c) = np.where(self.state == i)
            (gr, gc) = np.where(goal_state == i)
            distances.append(abs(gr - r) + abs(gc - c))
        return int(sum(distances))

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
def lowest_cost_successor(state):
    nodes = []
    same_cost = []
    (r1, c1, r2, c2) = tile_above(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2)))
    (r1, c1, r2, c2) = tile_below(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2)))
    (r1, c1, r2, c2) = tile_right(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2)))
    (r1, c1, r2, c2) = tile_left(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2)))
    lowest = nodes[0]
    num_nodes = len(nodes)
    if (num_nodes > 1):
        for i in range(1, num_nodes):
            if nodes[i].h_cost < lowest.h_cost:
                lowest = nodes[i]
    same_cost.append(lowest)
    for i in range(0, num_nodes):
        if nodes[i].h_cost == lowest.h_cost:
            same_cost.append(nodes[i])
    return random.choice(same_cost)


def hill_climbing():
    current = Node(init_state)
    print("Node: ", current.state)
    while True:
        neighbor = lowest_cost_successor(current.state)
        print_pattern(neighbor.state)
        print(f"Curr h: {current.h_cost}, Neigh h: {neighbor.h_cost}")
        if current.h_cost <= neighbor.h_cost:
            return current.state
        current = Node(neighbor.state)

print('Initial state:\n')
solution_state = hill_climbing()
print_pattern(solution_state)
print("\n*** Solved ***")
print('Goal state:\n')
print_pattern(goal_state)

# EOF.
