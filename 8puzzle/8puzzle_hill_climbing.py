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
        self.h_cost = self.heuristic_cost()

    # Heuristic used: 'Manhattan Distance'
    def heuristic_cost(self):
        # Tile 0.
        (t0_r, t0_c) = np.where(self.state == 0)
        (t0_gr, t0_gc) = np.where(goal_state == 0)
        t0_dis = abs(t0_gr - t0_r) + abs(t0_gc - t0_c)
        # Tile 1.
        (t1_r, t1_c) = np.where(self.state == 1)
        (t1_gr, t1_gc) = np.where(goal_state == 1)
        t1_dis = abs(t1_gr - t1_r) + abs(t1_gc - t1_c)
        # Tile 2.
        (t2_r, t2_c) = np.where(self.state == 2)
        (t2_gr, t2_gc) = np.where(goal_state == 2)
        t2_dis = abs(t2_gr - t2_r) + abs(t2_gc - t2_c)
        # Tile 3.
        (t3_r, t3_c) = np.where(self.state == 3)
        (t3_gr, t3_gc) = np.where(goal_state == 3)
        t3_dis = abs(t3_gr - t3_r) + abs(t3_gc - t3_c)
        # Tile 4.
        (t4_r, t4_c) = np.where(self.state == 4)
        (t4_gr, t4_gc) = np.where(goal_state == 4)
        t4_dis = abs(t4_gr - t4_r) + abs(t4_gc - t4_c)
        # Tile 5.
        (t5_r, t5_c) = np.where(self.state == 5)
        (t5_gr, t5_gc) = np.where(goal_state == 5)
        t5_dis = abs(t5_gr - t5_r) + abs(t5_gc - t5_c)
        # Tile 6.
        (t6_r, t6_c) = np.where(self.state == 6)
        (t6_gr, t6_gc) = np.where(goal_state == 6)
        t6_dis = abs(t6_gr - t6_r) + abs(t6_gc - t6_c)
        # Tile 7.
        (t7_r, t7_c) = np.where(self.state == 7)
        (t7_gr, t7_gc) = np.where(goal_state == 7)
        t7_dis = abs(t7_gr - t7_r) + abs(t7_gc - t7_c)
        # Tile 8.
        (t8_r, t8_c) = np.where(self.state == 8)
        (t8_gr, t8_gc) = np.where(goal_state == 8)
        t8_dis = abs(t8_gr - t8_r) + abs(t8_gc - t8_c)
        return sum([t0_dis, t1_dis, t2_dis, t3_dis, t4_dis, t5_dis, t6_dis, t7_dis, t8_dis])

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
print('Goal state:\n')
print_pattern(goal_state)
n = Node(init_state)
print(f"Node hc: {n.h_cost}")
#solution_state = hill_climbing()
#print_pattern(solution_state)
print("\n*** Solved ***")

# EOF.
