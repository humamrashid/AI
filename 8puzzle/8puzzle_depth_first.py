#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-puzzle using depth-first search. Specifically, an iterative-deepening depth-limited
# search is implemented. This implementation is a specialized version of general tree-search. No
# heuristic is used in this implementation.
# The tile board is represented as a 2D array with elements numbered according to the tile and the
# blank space has the value 0.

import numpy as np
import itertools
from enum import Enum

# Initial state (predefined)
init_state = np.array([(1,4,3), (7,8,0), (6,2,5)])

# Goal state (predefined)
goal_state = np.array([(1,2,3), (8,0,4), (7,6,5)])

# Search tree node structure.
class Node:
    def __init__(self, state, parent, action, cost):
        self.state = state
        self.parent = parent
        self.action = action
        self.path_cost = cost

# Types of "no solution found", either failure or cutoff because of depth-limit.
class NoSolution(Enum):
    CUTOFF = "cutoff"
    FAILURE = "failure"

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

# Follow the child node back to the parent and stack the chain.
def solution(node):
    print("solution found, building solution stack...", end="")
    solution_stack = []
    solution_stack.append(node)
    p = node.parent
    while p != None:
        solution_stack.append(p)
        p = p.parent
    print("done:")
    return solution_stack

# Test if the given state matches goal state.
def goal_test(state):
    return True if np.array_equal(state, goal_state) else False

def recursive_dls(node, limit):
    if goal_test(node.state):
        return solution(node)
    elif limit == 0:
        return NoSolution.CUTOFF
    else:
        cutoff = False
        actions = action_set(node.state)
        for act in actions.items():
            child = child_node(node, act)
            result = recursive_dls(child, limit - 1)
            if result == NoSolution.CUTOFF:
                cutoff = True
            elif result != NoSolution.FAILURE:
                return result
        return NoSolution.CUTOFF if cutoff else NoSolution.FAILURE

def depth_limited(limit):
    return recursive_dls(Node(init_state, None, None, 0), limit)

def iterative_deep():
    for depth in itertools.count():
        print(f"Trying depth: {depth}...", end="")
        result = depth_limited(depth)
        if result != NoSolution.CUTOFF:
            return result
        else:
            print("no solution found")

print('Initial state:\n')
print_pattern(init_state)
print()
solution = iterative_deep()
if solution == NoSolution.FAILURE:
    print("Failed to find solution!")
else:
    while len(solution) != 0:
        n = solution.pop()
        if n.action != None:
            print(f"\n{n.action}:\n")
            print_pattern(n.state)
    print(f"\n*** Solved ***\nPath Cost: {n.path_cost}")

# EOF.
