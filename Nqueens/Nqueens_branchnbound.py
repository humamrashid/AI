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
board_matrix = np.zeros((N, N), dtype=np.int8)

# Matrix for keeping track of major diagonal (\) in main board.
major_diag_matrix = np.empty((N, N), dtype=np.int8)
for i in range(0, N):
    for j in range(0, N):
        major_diag_matrix[i][j] = i - j + (N - 1)

# Matrix for keeping track of minor diagonal (/) in main board.
minor_diag_matrix = np.empty((N, N), dtype=np.int8)
for i in range(0, N):
    for j in range(0, N):
        minor_diag_matrix[i][j] = i + j

# Print the board as a simple grid.
def print_board(board):
    for i in range(0, N):
        for j in range(0, N):
            print(f"{board[i][j]}", end=" ")
        print()
    print()

def place_queens(board):
    return board_matrix

print("Original board:\n")
print_board(board_matrix)
print(f"Board after placing {N} queens:\n")
print_board(place_queens(board_matrix))

# EOF.
