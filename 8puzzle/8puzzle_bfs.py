#!/usr/bin/python3

# Solution for 8-puzzle.

import numpy as np
from collections import deque

# 8-puzzle is represented as a 2D array, initialized with default values representing the initial
# state (numbered tiles). A value of 0 indicates the blank tile. This is the 'world configuration'.
puzzle = np.array([(1,4,3), (7,8,0), (6,2,5)])

init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

done = False

# Tracking positions of the tiles in the 'world configuration'. 0-value tile is the blank space.
# Initial values match the initial state.
tiles = {
        0: (1, 2),
        1: (0, 0),
        2: (2, 1),
        3: (0, 2),
        4: (0, 1),
        5: (2, 2),
        6: (2, 0),
        7: (1, 0),
        8: (1, 1)
        }

# Queue for 'frontier' or 'open list'.
frontier = deque()

# Set for 'explored' set or 'closed list'.
explored = set()

# Search tree node structure.
class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = cost

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
def tile_above(t):
    global tiles
    row, col = tiles[t][0], tiles[t][1]
    for k, v in tiles.items():
        if (v[1] == col) and (row - v[0] == 1):
            return k
    return -1

# Is there another tile on the same col., one row below?
def tile_below(t):
    global tiles
    row, col = tiles[t][0], tiles[t][1]
    for k, v in tiles.items():
        if (v[1] == col) and (v[0] - row == 1):
            return k
    return -1

# Is there another tile on the same row, one col. right?
def tile_right(t):
    global tiles
    row, col = tiles[t][0], tiles[t][1]
    for k, v in tiles.items():
        if (v[0] == row) and (v[1] - col == 1):
            return k
    return -1

# Is there another tile on the same row, one col. left?
def tile_left(t):
    global tiles
    row, col = tiles[t][0], tiles[t][1]
    for k, v in tiles.items():
        if (v[0] == row) and (col - v[1] == 1):
            return k
    return -1

# Switch values and positions of tiles t1 and t2.
def switch_tiles(t1, t2):
    global puzzle, tiles
    tmp_pos = tiles[t1]
    tmp_val = puzzle[tmp_pos[0], tmp_pos[1]]
    puzzle[tmp_pos[0], tmp_pos[1]] = puzzle[tiles[t2][0], tiles[t2][1]]
    puzzle[tiles[t2][0], tiles[t2][1]] = tmp_val
    tiles[t1] = tiles[t2]
    tiles[t2] = tmp_pos

# Move blank tile up.
def move_up():
    global tiles
    t = tile_above(0)
    if t != -1:
        switch_tiles(0, t)
        return True
    return False

# Move blank tile down.
def move_down(t):
    global tiles
    t = tile_below(0)
    if t != -1:
        switch_tiles(0, t)
        return True
    return False

# Move blank tile right.
def move_right(t):
    global tiles
    t = tile_right(0)
    if t != -1:
        switch_tiles(0, t)
        return True
    return False

# Move blank tile left.
def move_left(t):
    global tiles
    t = tile_left(0)
    if t != -1:
        switch_tiles(0, t)
        return True
    return False

action_set = {
        'up':    move_up,
        'down':  move_down,
        'right': move_right,
        'left':  move_left
        }

def result(state, action):
    global puzzle
    puzzle = state.copy()

def child_node(parent, action):
    return Node(result(parent.state, action), parent, action, parent.path_cost, + 1)

def actions(state):
    return

def empty(struct):
    return True if len(struct) == 0 else False

def add_explored(state):
    explored.add(tuple(map(tuple, state)))

def in_explored(state):
    s = tuple(map(tuple, state))
    return True if s in explored else False

def in_frontier(s):
    for node in frontier:
        if np.array_equal(node.state, s):
            return True
    return False

def solution(node):
    global done
    solution_stack = []
    solution_stack.append(node.state)
    p = node.parent
    while p != None:
        solution_stack.append(p.state)
        p = p.parent
    while len(solution_stack) != 0:
        print_pattern(solution_stack.pop())
        print()
    done = True

def goal_test(state):
    global goal_state
    return True if np.array_equal(state, goal_state) else False

def breadth_first():
    global init_state, done
    node = Node(init_state, None, None, 0)
    if goal_test(node.state):
        solution(node)
    frontier.append(node)
    while not done:
       if empty(frontier):
           print("Failed to find solution!")
           done = True
       node = frontier.popleft()
       add_explored(node.state)
       for a in actions(node.state):
           child = child_node(node, a)
           #if not in_explored(child.state) and not in_frontier(child.state):
           #   if goal_test(child.state):
           #       solution(child)
           #   frontier.append(child)

def depth_first():
    return

print('Initial state:\n')
print_pattern(puzzle)
print(move_up())
print_pattern(puzzle)

# EOF.
