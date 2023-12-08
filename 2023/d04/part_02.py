import re
import numpy as np
from itertools import count, takewhile

with open("input.txt") as f:
    lines = f.read().strip().split("\n")

numbers = [list(map(int, re.findall(r"\d+", line))) for line in lines]
intersection_counts = [len(set(n[11:]) & set(n[1:11])) for n in numbers]

N = len(numbers)
rows, cols = np.ogrid[:N, :N]
mat = (cols > rows) & (cols <= rows + np.array(intersection_counts)[:, np.newaxis])

v = np.ones(N)
result = int(np.sum(list(takewhile(np.any, (v := mat @ v for _ in count())))) + N)
print(result)
