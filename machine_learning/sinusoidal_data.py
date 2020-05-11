#!/usr/bin/python3
# Author: Humam Rashid
# Curve-Fitting with least squares method.

import sys
import numpy as np
from numpy.polynomial import polynomial as pnl
import matplotlib.pyplot as plt

if len(sys.argv) != 4:
    print(f"Usage: <data_n> <pln_deg> <orig_n>")
    exit(1)

data_n = int(sys.argv[1])
pln_deg = int(sys.argv[2])
orig_n = int(sys.argv[3])
if data_n <= 0 or orig_n <= 0:
    print("Number of data points must be > 0")
    exit
if pln_deg < 0:
    print("Polynomial degree must be >= 0")
    exit(1)

# Original sinusodial curve sine(2*pi*x) of orig_n values from [0, 1].
original = np.linspace(0, 1, orig_n)

# Smaller sample of data_n values from [0, 1].
x = np.linspace(0, 1, data_n)

# Training data with small amount of Gaussian white noise.
t_data = np.random.normal(loc=x, scale=0.05, size=data_n)

# Least squares fitting.
coeff = pnl.polyfit(x, np.sin(2 * np.pi * t_data), pln_deg)
ffit = pnl.polyval(x, coeff)

# Plot original sinusoidal, scatter plot of data points and least squares fit.
plt.plot(original, np.sin(2 * np.pi * original), color='green')
plt.scatter(x, np.sin(2 * np.pi * t_data), color='blue', label=f"N = {data_n}")
plt.plot(x, ffit, color='red', label=f"M = {pln_deg}")

# Viewing setttings.
plt.xlabel('x')
plt.ylabel('t')
plt.axis('tight')
plt.xlim(0, 1)
plt.ylim(-1, 1)
plt.legend()
plt.show()

# EOF.
