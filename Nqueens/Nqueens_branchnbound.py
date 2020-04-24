#!/usr/bin/python3
# Author: Humam Rashid

# Solution for 8-queens problem using branch and bound method.

import numpy as np

# Ask user for board size.
print("Enter N for NxN board: ", end="")
N = int(input())

# Main board matrix for placing N
board_matrix = np.zeros((N, N))
right_diag_matrix = np.empty((N, N))
left_diag_matrix = np.empty((N, N))

print(board_matrix)

# EOF.
