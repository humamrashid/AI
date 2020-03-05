#!/usr/bin/python3

# Solution for 8-puzzle.

from collections import deque

# 8-puzzle is represented as a 2D tuple, initialized with default values representing the initial
# state (numbered tiles). A value of 0 indicates the blank tile. This is the 'world configuration'.
puzzle = ((1,4,3), (7,8,0), (6,2,5))

# Intial state (pre-determined).
init_state = ((1,4,3), (7,8,0), (6,2,5))
# Goal state (pre-determined).
goal_state = ((1,2,3), (8,0,4), (7,6,5))

done = False

# Tracking positions of the tiles. 0-value tile is the blank space.
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

# Hashtable for 'explored' set or 'closed list'.
explored = set()
explored.add(puzz)

# Search tree node structure.
class Node:
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

# Print a tile pattern with current values.
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
    return True if pos[1] == tiles[0][1] and (pos[0] - tiles[0][0] == 1) else False

# Sample col., one row below.
def blank_below(pos):
    return True if pos[1] == tiles[0][1] and (tiles[0][0] - pos[0] == 1) else False

# Same row, one col. right.
def blank_right(pos):
    return True if pos[0] == tiles[0][0] and (tiles[0][1] - pos[1] == 1) else False

# Same row, one col. left
def blank_left(pos):
    return True if pos[0] == tiles[0][0] and (pos[1] - tiles[0][1] == 1) else False

# Switch values and positions of tiles t1 and t2.
def switch_tiles(t1, t2):
    tmp_pos = tiles[t1]
    tmp_val = puzzle[tmp_pos[0], tmp_pos[1]]
    puzzle[tmp_pos[0], tmp_pos[1]] = puzzle[tiles[t2][0], tiles[t2][1]]
    puzzle[tiles[t2][0], tiles[t2][1]] = tmp_val
    tiles[t1] = tiles[t2]
    tiles[t2] = tmp_pos

def move_up(t):
    if blank_above(tiles[t]):
        switch_tiles(0, t)
        return True
    return False

def move_down(t):
    if blank_below(tiles[t]):
        switch_tiles(0, t)
        return True
    return False

def move_right(t):
    if blank_right(tiles[t]):
        switch_tiles(0, t)
        return True
    return False

def move_left(t):
    if blank_left(tiles[t]):
        switch_tiles(0, t)
        return True
    return False

def result(state, action):
    return

def child_node(parent, action):
    return Node(result(parent.state, action), parent, action)

def empty(struct):
    return True if len(struct) == 0 else False

def solution(node):
    return

def goal_test(state):
    return True if state == goal_state else False

def breadth_first():
    root = Node(init_state, None, None)
    if goal_test(root.state):
        solution(root)
    frontier.append(root)
    while not done:
        if empty(frontier):
            print("Failed to find solution")
            done = True
        node = frontier.popleft()
        explored.add(node.state)



print('Initial state:\n')
print_puzzle()
print(explored)
print('\nSolved')

# EOF.
