import numpy as np
import matplotlib.pyplot as plt
import time

plt.axis([0, 10, 0, 1])
plt.ion()

for i in range(10):
    y = np.random.random()
    plt.scatter(i, y, color = 'red')
    plt.pause(.05)
while True:
    plt.pause(.05)
