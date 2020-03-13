#!/usr/bin/python3

# Solution for 8-puzzle using breadth-first search. This implementation is a specialized version of
# general graph-search.
# The tile board is represented as a 2D array with elements numbered according to the tile and the
# blank space has the value 0.

import numpy as np
from collections import deque

# Initial state (predefined)
init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Goal state (predefined)
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

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

# Child node is based on the parent and action taken.
def child_node(parent, act):
    return Node(act[1], parent, act[0], parent.path_cost + 1)

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

# Returns possible action set, a mapping of directions ('up', 'down', 'left', 'right') to specific
# movements and the resulting states.
def action_set(state):
    actions = dict({'up': None, 'down': None, 'left': None, 'right': None})
    (r1, c1, r2, c2) = tile_above(state)
    if r1 != None:
        actions['up'] = switch_tiles(state, r1, c1, r2, c2)
    else:
        del actions['up']
    (r1, c1, r2, c2) = tile_below(state)
    if r1 != None:
        actions['down'] = switch_tiles(state, r1, c1, r2, c2)
    else:
        del actions['down']
    (r1, c1, r2, c2) = tile_right(state)
    if r1 != None:
        actions['right'] = switch_tiles(state, r1, c1, r2, c2)
    else:
        del actions['right']
    (r1, c1, r2, c2) = tile_left(state)
    if r1 != None:
        actions['left'] = switch_tiles(state, r1, c1, r2, c2)
    else:
        del actions['left']
    return actions

# Add something to the explored set.
def add_explored(state):
    explored.add(tuple(map(tuple, state)))

# Check if something is in the explored set or not.
def in_explored(state):
    s = tuple(map(tuple, state))
    return True if s in explored else False

# Check if something is in the frontier or not.
def in_frontier(s):
    for node in frontier:
        if np.array_equal(node.state, s):
            return True
    return False

# Check if a structure (e.g., frontier) is empty.
def empty(struct):
    return True if len(struct) == 0 else False

# Follow the child node back to the parent and stack the chain.
def solution(node):
    solution_stack = []
    solution_stack.append(node)
    p = node.parent
    while p != None:
        solution_stack.append(p)
        p = p.parent
    return solution_stack

# Test if the given state matches goal state.
def goal_test(state):
    return True if np.array_equal(state, goal_state) else False

def breadth_first():
    node = Node(init_state, None, None, 0)
    if goal_test(node.state):
        return solution(node)
    frontier.append(node)
    while True:
       if empty(frontier):
           return None
       node = frontier.popleft()
       add_explored(node.state)
       actions = action_set(node.state)
       for act in actions.items():
           child = child_node(node, act)
           if not in_explored(child.state) and not in_frontier(child.state):
               if goal_test(child.state):
                   return solution(child)
               frontier.append(child)

print('Initial state:\n')
print_pattern(init_state)
solution = breadth_first()
if solution == None:
    print("Failed to find solution!")
else:
    while len(solution) != 0:
        n = solution.pop()
        if n.action != None:
            print(f"\n{n.action}:\n")
            print_pattern(n.state)
    print(f"\n*** Solved ***\nPath Cost: {n.path_cost}")

# EOF.
