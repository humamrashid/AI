#!/usr/bin/python3

# Implementation of farmer, fox, goose and grain problem solution using simple reflex agent method.

import random

# States:
# 0 indicates 'at starting point', 1 indicates 'at ending point'.
# 1st digit is farmer, 2nd is fox, 3rd is goose and 4th is grain. Initially, everyone starts at 0.
#
# 0000 = VALID      (Start state)
# 0001 = VALID
# 0010 = VALID
# 0011 = INVALID
# 0100 = VALID
# 0101 = VALID
# 0110 = INVALID
# 0111 = INVALID
# 1000 = INVALID
# 1001 = INVALID
# 1010 = VALID
# 1011 = VALID
# 1100 = INVALID
# 1101 = VALID
# 1110 = VALID
# 1111 = VALID      (Goal state)
states = {
        "Farmer":   0,
        "Fox":      0,
        "Goose":    0,
        "Grain":    0
        }

# 000 = VALID
# 001 = VALID
# 010 = VALID
# 011 = VALID OR INVALID if farmer not there.
# 100 = VALID OR INVALID if farmer there.
# 101 = VALID
# 110 = VALID OR INVALID if farmer not there.
# 111 = VALID OR INVALID if farmer not there.

# Indicates successful transition from starting point to finishing point; initially false.
transit = False

# Percepts are the states directly, no need to interpret.
def simple_reflex_agent():
    # Rules:
    if states["Fox"] == 1 and states["Goose"] == 1 and states["Farmer"] == 0:
        return False
    elif states["Goose"] == 1 and states["Grain"] == 1 and states["Farmer"] == 0:
        return False
    elif states["Farmer"] == 1 and states["Fox"] == 0 and states["Goose"] == 0:
        return False
    elif states["Farmer"] == 1 and states["Goose"] == 0 and states["Grain"] == 0:
        return False
    return True

for s in states:
    for i in range(0, 2):
        for j in range(0, 2):
            states[s] = j
            if simple_reflex_agent():
                print(states)

# EOF.
