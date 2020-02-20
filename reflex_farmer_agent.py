#!/usr/bin/python3

# Implementation of farmer, fox, goose and grain problem solution using simple reflex agent method.

import enum
import random

# River banks: A is the starting point, B is the destination.

# States:
# (Farmer = FR, Fox = FO, Goose = GO, Grain = GR)
#
# 0  = (FR, FO, GO, GR) on A, () on  B  (Valid)
# 1  = (FR, FO, GO) on A, (GR) on B     (Valid)
# 2  = (FR, FO, GR) on A, (GO) on B     (Valid)
# 3  = (FR, GR, GO) on A, (FO) on B     (Valid)
# 4  = (FO, GR, GO) on A, (FR) on B     (Invalid)
# 5  = (FR, FO) on A, (GO, GR) on B     (Invalid)
# 6  = (FR, GR) on A, (FO, GO) on B     (Invalid)
# 7  = (FR, GO) on A, (FO, GR) on B     (Valid)
# 8  = (FO, GR) on A, (FR, GO) on B     (Valid)
# 9  = (FO, GO) on A, (FR, GR) on B     (Invalid)
# 10 = (GR, GO) on A, (FR, FO) on B     (Invalid)
# 11 = (FR) on A, (FO, GR, GO) on B     (Invalid)
# 12 = (FO) on A, (FR, GR, GO) on B     (Valid)
# 13 = (GR) on A, (FR, FO, GO) on B     (Valid)
# 14 = (GO) on A, (FR, FO, GR) on B     (Valid)
# 15 = () on A, (FR, FO, GR, GO) on B   (Valid)

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

while not is_trip_done():
    farmer_agent()
print("*** Trip Completed Successfully ***")

# EOF.
