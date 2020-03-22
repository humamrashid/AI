#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-puzzle using iterative random-restart hill-climbing; heuristic used is 'Manhattan
# distance.' The tile board is represented as a 2D array with elements numbered according to the
# tile and the blank space has the value 0.

import numpy as np
import random
import itertools

# Initial state (predefined)
init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Goal state (predefined)
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

# Search tree node structure.
class Node:
    def __init__(self, state, direction):
        self.state = state
        self.direction = direction
        self.h_cost = self.manhattan_distance()
    def manhattan_distance(self):
        if self.state is None:
            return None
        distances = []
        for i in range(0, 9):
            (r, c) = np.where(self.state == i)
            (gr, gc) = np.where(goal_state == i)
            distances.append(abs(gr - r) + abs(gc - c))
        return int(sum(distances))

# A 'solution' state, indicates if a solution state was found or the state is closer intermediary
# stage.
class Solution:
    def __init__(self, node, found, update):
        self.node = node
        self.found = found
        self.update = update

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

# Returns either lowest cost successor or random one, with preference for the former.
def successor(state):
    nodes = []
    same_cost = []
    (r1, c1, r2, c2) = tile_above(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2), 'up'))
    (r1, c1, r2, c2) = tile_below(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2), 'down'))
    (r1, c1, r2, c2) = tile_right(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2), 'right'))
    (r1, c1, r2, c2) = tile_left(state)
    if r1 != None:
        nodes.append(Node(switch_tiles(state, r1, c1, r2, c2), 'left'))
    r = random.choice([0, 1, 2, 3])
    if r == 0:
        return random.choice(nodes)
    lowest = nodes[0]
    num_nodes = len(nodes)
    if (num_nodes > 1):
        for i in range(1, num_nodes):
            if nodes[i].h_cost <= lowest.h_cost:
                lowest = nodes[i]
        same_cost.append(lowest)
        for i in range(0, num_nodes):
            if nodes[i].h_cost == lowest.h_cost:
                same_cost.append(nodes[i])
        if len(same_cost) > 1:
            return random.choice(same_cost)
    return lowest

def hill_climbing(state, limit):
    count = 0;
    current = Node(state, None)
    lowest = current
    updated = False
    while count < limit:
        if current.h_cost == 0:
            return Solution(current, True, False)
        if current.h_cost <= lowest.h_cost:
            lowest = current
            updated = True
        neighbor = successor(current.state)
        if neighbor.direction is not None:
            print(f"{neighbor.direction}:\n")
        print_pattern(neighbor.state)
        print()
        current = neighbor
        count += 1
    if updated:
        return Solution(lowest, False, True)
    return Solution(None, False, False)

def iterative_random_restart():
    result = Solution(None, False, False)
    for limit in itertools.count():
        if result.found == True:
            return result.node
        if result.update == False:
            random_state = init_state
        else:
            random_state = result.node.state
        np.random.shuffle(random_state)
        result = hill_climbing(random_state, limit)

print('Initial state:\n')
print_pattern(init_state)
print()
solution = iterative_random_restart()
if solution.direction is not None:
    print(f"{solution.direction}:\n")
print_pattern(solution.state)
print("\n*** Solved ***")

# EOF.
