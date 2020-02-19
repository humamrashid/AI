#!/usr/bin/python3

# Implementation of farmer, fox, goose and grain problem solution using simple reflex agent method.

# River banks: A is the starting point, B is the destination.

# States:
# (Frrmer = Fr, Fox = Fo, Goose = Go, Grain = Gr)
#
# 0  = (Fr, Fo, Go, Gr) on A, () on  B  (Valid)
# 1  = (Fr, Fo, Go) on A, (Gr) on B     (Valid)
# 2  = (Fr, Fo, Gr) on A, (Go) on B     (Valid)
# 3  = (Fr, Gr, Go) on A, (Fo) on B     (Valid)
# 4  = (Fo, Gr, Go) on A, (Fr) on B     (Invalid)
# 5  = (Fr, Fo) on A, (Go, Gr) on B     (Invalid)
# 6  = (Fr, Gr) on A, (Fo, Go) on B     (Invalid)
# 7  = (Fr, Go) on A, (Fo, Gr) on B     (Valid)
# 8  = (Fo, Gr) on A, (Fr, Go) on B     (Valid)
# 9  = (Fo, Go) on A, (Fr, Gr) on B     (Invalid)
# 10 = (Gr, Go) on A, (Fr, Fo) on B     (Invalid)
# 11 = (Fr) on A, (Fo, Gr, Go) on B     (Invalid)
# 12 = (Fo) on A, (Fr, Gr, Go) on B     (Valid)
# 13 = (Gr) on A, (Fr, Fo, Go) on B     (Valid)
# 14 = (Go) on A, (Fr, Fo, Gr) on B     (Valid)
# 15 = () on A, (Fr, Fo, Gr, Go) on B   (Valid)

on_boat = {
        "fr": ("Farmer"),
        "frgo": ("Farmer", "Goose"),
        "frgr": ("Farmer", "Grain"),
        "frfo": ("Farmer", "Fox"),
        }

def take(bank, group):
    print(f"Take {group} to {bank}")

def reflex_farmer_agent(state):
    if location == "A":
        take(location, on_boat[1])


reflex_farmer_agent("A")

# EOF.
