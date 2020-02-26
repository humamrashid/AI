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

# Indicates successful transition from starting point to finishing point; initially false.
transit = False

def reset():
    for s in states:
        states[s] = 0
    print("*** RESET ***")

def simple_reflex_agent():
    global transit
    # Rules:
    if states["Fox"] == 1 and states["Goose"] == 1 and states["Farmer"] == 0:
        transit = False
        reset()
    elif states["Goose"] == 1 and states["Grain"] == 1 and states["Farmer"] == 0:
        transit = False
        reset()
    elif states["Farmer"] == 1 and states["Fox"] == 0 and states["Goose"] == 0:
        transit = False
        reset()
    elif states["Farmer"] == 1 and states["Goose"] == 0 and states["Grain"] == 0:
        transit = False
        reset()
    elif states["Farmer"] == 0 or states["Fox"] == 0 or states["Goose"] == 0 or states["Grain"] == 0:
        transit = False
    else:
        transit = True

while not transit:
    if states["Farmer"] == 0:
        states["Farmer"] = 1
        print("Farmer crosses river", end=" ")
    else:
        states["Farmer"] = 0
        print("Farmer goes back", end=" ")
    if states["Farmer"] == 1:
        c = random.choice(["Fox", "Goose", "Grain"])
        if states[c] != 1:
            states[c] = 1
            print(f"with {c}")
        print()
    elif states["Farmer"] == 0:
        c = random.choice(["Fox", "Goose", "Grain"])
        if states[c] != 0:
            states[c] = 0
            print(f"with {c}")
        print()
    simple_reflex_agent()
    #print(states)

print("*** Success ***")

# EOF.
