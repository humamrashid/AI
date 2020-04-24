#!/usr/bin/python3
# Author: Humam Rashid

# Solution for N-queens problem using branch and bound method.

import sys
import numpy as np

# Get board size.
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <N>")
    exit(1)
N = int(sys.argv[1])

# Main board matrix for placing N queens.
board_matrix = np.zeros((N, N))

# Matrix for keeping track of major diagonal (\) in main board.
major_diag_matrix = np.empty((N, N))
# Matrix for keeping track of minor diagonal (/) in main board.
minor_diag_matrix = np.empty((N, N))

print(board_matrix)

# EOF.
