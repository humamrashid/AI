#!/usr/bin/python3
# Author: Humam Rashid
# Curve-Fitting with least squares method.

import numpy as np
import matplotlib.pyplot as plt
from numpy.polynomial import polynomial as pnl

# Original sinusodial curve sine(2*pi*x) with 100 values from [0, 1].
original = np.linspace(0, 1, 100)

# Smaller sample of 10 values from [0, 1] with Gaussian white noise. Standard deviation of 0.05 used
# to keep amount of noise "small."
x = np.linspace(0, 1, 40)
x_noise = np.random.normal(loc=x, scale=0.05, size=40)

# Least squares fitting.
c = pnl.polyfit(x, np.sin(2*np.pi*x_noise), 15)
ffit = pnl.polyval(x, c)

# Plot original sinusoidal, scatter plot of data points and least squares fit.
plt.plot(original, np.sin(2*np.pi*original), color='green')
plt.scatter(x, np.sin(2*np.pi*x_noise), color='blue')
plt.plot(x, ffit, color='red')

# Viewing setttings.
plt.xlabel('x')
plt.ylabel('t')
plt.axis('tight')
plt.xlim(0, 1)
plt.ylim(-1, 1)
plt.show()

# EOF.
