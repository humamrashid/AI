#!/usr/bin/python3
# Author: Humam Rashid

# Solution for N-queens problem using branch and bound method.

import numpy as np

# Ask user for board size.
print("Enter N for NxN board: ", end="")
N = int(input())

# Main board matrix for placing N queens.
board_matrix = np.zeros((N, N))

# Matrix for keeping track of major diagonal (\) in main board.
major_diag_matrix = np.empty((N, N))
# Matrix for keeping track of minor diagonal (/) in main board.
minor_diag_matrix = np.empty((N, N))

print(board_matrix)

# EOF.
