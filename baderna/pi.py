import numpy as np
from time import time
from random import random

inside = 0
n = 100000000000000000

t_0 = time()
for i in range(n):
    x, y = random(), random()
    if x**2 + y**2 < 1:
        inside += 1
print(np.round(time()-t_0, 3), "seconds elapsed for naive method and n=", n)
print("pi is roughly", inside/n*4)