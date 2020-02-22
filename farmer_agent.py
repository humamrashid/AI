#!/usr/bin/python3

# Implementation of farmer, fox, goose and grain problem solution using simple reflex agent method.

import enum
import random

# 5-digit binary number used to represent states.
# 1st digit (from left): 0 is the starting point, 1 is the destination.
# 2nd digit (from left): 1 farmer present,        0 farmer not present.
# 3rd digit (from left): 1 fox present,           0 fox not present.
# 4th digit (from left): 1 goose present,         0 goose not present.
# 5th digit (from left): 1 grain present,         0 grain not present.

# States:
# (Farmer = FR, Fox = FO, Goose = GO, Grain = GR)
# (River banks: starting at A, ending in B)
#

# (FR, FO, GO, GR) on A, () on  B  (Valid)      = 01111 = 10000 = Start state
# (FR, FO, GO) on A, (GR) on B     (Valid)      = 01110 = 10001
# (FR, FO, GR) on A, (GO) on B     (Valid)      = 01101 = 10010
# (FR, FO) on A, (GO, GR) on B     (Invalid)    = 01100 = 10011
# (FR, GO, GR) on A, (FO) on B     (Valid)      = 01011 = 10100
# (FR, GO) on A, (FO, GR) on B     (Valid)      = 01010 = 10101
# (FR, GR) on A, (FO, GO) on B     (Invalid)    = 01001 = 10110
# (FR) on A, (FO, GR, GO) on B     (Invalid)    = 01000 = 10111
# (FO, GR, GO) on A, (FR) on B     (Invalid)    = 00111 = 11000
# (FO, GO) on A, (FR, GR) on B     (Invalid)    = 00110 = 11001
# (FO, GR) on A, (FR, GO) on B     (Valid)      = 00101 = 11010
# (FO) on A, (FR, GR, GO) on B     (Valid)      = 00100 = 11011
# (GR, GO) on A, (FR, FO) on B     (Invalid)    = 00011 = 11100
# (GO) on A, (FR, FO, GR) on B     (Valid)      = 00010 = 11101
# (GR) on A, (FR, FO, GO) on B     (Valid)      = 00001 = 11110
# () on A, (FR, FO, GR, GO) on B   (Valid)      = 00000 = 11111 = Goal state
#
# Decimal equivalent (12, 19), (9, 22), (8, 23), (7, 24), (6, 25), (3, 28) are invalid.

class GROUP(enum.Enum):
    FR = "Farmer"
    FO = "Fox"
    GO = "Goose"
    GR = "Grain"

class BANK(enum.Enum):
    A = "River Bank A"
    B = "River Bank B"

# Tracking the current location of all participants; initially everyone starts on river bank A.
curr_loc = {
        GROUP.FR:   BANK.A,
        GROUP.FO:   BANK.A,
        GROUP.GO:   BANK.A,
        GROUP.GR:   BANK.A
        }

# Things that can be on the boat: the farmer and at most one other thing among the group of three.
on_boat = {
        "FR":   (GROUP.FR,),
        "FRFO": (GROUP.FR, GROUP.FO),
        "FRGO": (GROUP.FR, GROUP.GO),
        "FRGR": (GROUP.FR, GROUP.GR)
        }

# Take members of 'GROUP' to one of the river 'BANK's.
def take(group, bank):
    print(f"Taking {[m.value for m in group]} to {bank.value}")
    for m in group:
        curr_loc[m] = bank
        print(f"|--{m.value} is now on {curr_loc[m].value}")

# Check if the trip is done; the trip is considered done when all members of GROUP are on river BANK
# B.
def is_trip_done():
    for m in GROUP:
        if curr_loc[m] != BANK.B:
            return False
    return True

# Farmer agent's actions in step 3 and 5 are randomized.
def farmer_agent():
    take(on_boat["FRGO"], BANK.B)
    take(on_boat["FR"], BANK.A)
    fox_first = random.choice([True, False])
    if fox_first:
        take(on_boat["FRFO"], BANK.B)
    else:
        take(on_boat["FRGR"], BANK.B)
    take(on_boat["FRGO"], BANK.A)
    if fox_first:
        take(on_boat["FRGR"], BANK.B)
    else:
        take(on_boat["FRFO"], BANK.B)
    take(on_boat["FR"], BANK.A)
    take(on_boat["FRGO"], BANK.B)

# EOF.
