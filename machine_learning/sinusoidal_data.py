#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt
import random

x = np.linspace(0, 1, 50)
x_noise = np.random.normal(loc=x, scale=0.1, size=50)

plt.plot(x, np.sin(2*np.pi*x))
plt.scatter(x, np.sin(2*np.pi*x_noise))
plt.xlabel('x')
plt.ylabel('t')
plt.axis('tight')
plt.show()

# EOF.
