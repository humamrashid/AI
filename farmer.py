#!/usr/bin/python3

# Implementation of farmer, fox, goose and grain problem solution using simple reflex agent method.

# River banks: A is the starting point, B is the destination.

# States:
# (Farmer = Fa, Fox = Fo, Goose = Go, Grain = Gr)
#
# 0  = (Fa, Fo, Go, Gr) on A, () on  B  (Valid)
# 1  = (Fa, Fo, Go) on A, (Gr) on B     (Valid)
# 2  = (Fa, Fo, Gr) on A, (Go) on B     (Valid)
# 3  = (Fa, Gr, Go) on A, (Fo) on B     (Valid)
# 4  = (Fo, Gr, Go) on A, (Fa) on B     (Invalid)
# 5  = (Fa, Fo) on A, (Go, Gr) on B     (Invalid)
# 6  = (Fa, Gr) on A, (Fo, Go) on B     (Invalid)
# 7  = (Fa, Go) on A, (Fo, Gr) on B     (Valid)
# 8  = (Fo, Gr) on A, (Fa, Go) on B     (Valid)
# 9  = (Fo, Go) on A, (Fa, Gr) on B     (Invalid)
# 10 = (Gr, Go) on A, (Fa, Fo) on B     (Invalid)
# 11 = (Fa) on A, (Fo, Gr, Go) on B     (Invalid)
# 12 = (Fo) on A, (Fa, Gr, Go) on B     (Valid)
# 13 = (Gr) on A, (Fa, Fo, Go) on B     (Valid)
# 14 = (Go) on A, (Fa, Fo, Gr) on B     (Valid)
# 15 = () on A, (Fa, Fo, Gr, Go) on B   (Valid)

on_boat = {
        0: ("Farmer"),
        1: ("Farmer", "Goose"),
        2: ("Farmer", "Grain"),
        3: ("Farmer", "Fox"),
        }

def take(bank, group):
    print(f"Take {group} to {bank}")

# parameters: location
# returns:    action
def reflex_farmer_agent(location):
    if location == "A":
        take(location, on_boat[1])


reflex_farmer_agent("A")

# EOF.
