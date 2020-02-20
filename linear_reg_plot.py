#!/usr/bin/python3

# Sample linear regression plotting with numpy.
# x values are 50 randomly picked floating point values within a range.
# y values are randomly picked to be the same value as x or x plus/minus 1.

import numpy as np
import matplotlib.pyplot as plt
import random

x = []
y = []
for i in range(0, 50):
    c = random.choice([0, 1, 2])
    x.append(random.uniform(-5, 6))
    if c == 1:
        y.append(x[i] + 1)
    elif c == 2:
        y.append(x[i] - 1)
    else:
        y.append(x[i])

coef = np.polyfit(x, y, 1)
poly1d_fn = np.poly1d(coef)

plt.plot(x,y, 'yo', x, poly1d_fn(x), '--k')
plt.xlim(-5, 6)
plt.ylim(-5, 6)

plt.show()

# EOF.
