#!/usr/bin/python3
# Author: Humam Rashid
# Curve-Fitting with least squares method.

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as pnl

# Constants.
ORIG_N = 100
DATA_N = 10
PLN_DEG = 0

# Original sinusodial curve sine(2*pi*x) of ORIG_N values from [0, 1].
original = np.linspace(0, 1, ORIG_N)

# Smaller sample of DATA_N values from [0, 1].
x = np.linspace(0, 1, DATA_N)

# Training data with small amount of Gaussian white noise.
t_data = np.random.normal(loc=x, scale=0.05, size=DATA_N)

# Least squares fitting.
coeff = pnl.polyfit(x, np.sin(2*np.pi*t_data), PLN_DEG)
ffit = pnl.polyval(x, coeff)

# Plot original sinusoidal, scatter plot of data points and least squares fit.
plt.plot(original, np.sin(2 * np.pi * original), color='green')
plt.scatter(x, np.sin(2 * np.pi * t_data), color='blue', label=f"N = {DATA_N}")
plt.plot(x, ffit, color='red', label=f"M = {PLN_DEG}")

# Viewing setttings.
plt.xlabel('x')
plt.ylabel('t')
plt.axis('tight')
plt.xlim(0, 1)
plt.ylim(-1, 1)
plt.legend()
plt.show()

# EOF.
