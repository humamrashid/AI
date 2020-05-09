#!/usr/bin/python3

import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0, 1, 10)
x2 = np.linspace(0, 1, 10)

samples = np.random.normal(size=10)

plt.plot(x1, np.sin(2*np.pi*x1))
plt.scatter(x1, np.sin(2*np.pi*samples))
plt.xlabel('x')
plt.ylabel('t')
plt.axis('tight')
plt.show()

# EOF.
