#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-queens problem using uniform-cost branch and bound method.

import numpy as np
import heapq as pq
import random

# Initial state (empty board)
init_state = np.zeros((8, 8), dtype=np.int8)

# Goal state (predefined in problem description)
goal_state = np.zeros((8, 8), dtype=np.int8)
goal_state[0][0] = 1
goal_state[1][6] = 1
goal_state[2][4] = 1
goal_state[3][7] = 1
goal_state[4][1] = 1
goal_state[5][3] = 1
goal_state[6][5] = 1
goal_state[7][2] = 1

# 'Frontier' or 'open list', treated as a priority queue.
frontier = []

# 'Explored set' or 'closed list'.
explored = set()

# Search tree node structure.
class Node:
    def __init__(self, state, parent, cost):
        self.state = state
        self.parent = parent
        self.path_cost = cost

def child_node(parent, act):
    state = np.zeros((8, 8), dtype=np.int8)
    transpose = state.T
    for i in range(8):
        transpose[i][random.choice([0, 1, 2, 3, 4, 5, 6, 7])] = 1
    return Node(state, parent, parent.path_cost + 1)

# Print a tile pattern from given 'state'.
def print_board(state):
    for i in range(8):
        for j in range(8):
            print(state[i][j], end="  ")
        print()

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
    print("Building solution stack...", end="")
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

def uniform_cost():
    node = Node(init_state, None, None, 0)
    frontier.append(node)
    heappush(frontier, (node.path_cost, node))
    while True:
       if empty(frontier):
           return None
       (_, node) = heappop(frontier)
       if goal_test(node.state):
           return solution(node)
       add_explored(node.state)
       child = child_node(node)
       if not in_explored(child.state) and not in_frontier(child):
           heappush(frontier, (child.path_cost, child))
       else if in_frontier(child.state) and child.path_cost > node.path_cost:
           # replace that frontier node with child
           node = child

print('Initial state:\n')
print_board(init_state)
print()
solution = uniform_cost()
if solution == None:
    print("Failed to find solution!")
#else:
    #while len(solution) != 0:
        #n = solution.pop()
    #print(f"\n*** Solved ***\nPath Cost: {n.path_cost}")

# EOF.
