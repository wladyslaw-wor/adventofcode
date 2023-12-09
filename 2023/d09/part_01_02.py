import re
import numpy as np

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

ns = np.array([list(map(int, re.findall(r"-?\d+", x))) for x in ls])

for a in (ns, np.flip(ns, 1)):
    print(np.sum([np.diff(a, k)[:,-1] for k in range(ns.shape[1])]))