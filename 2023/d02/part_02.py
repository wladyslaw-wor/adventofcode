import math
import re
from collections import defaultdict

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

good_ids = 0
total_power = 0
for l in ls:
    parts = re.sub("[;,:]", "", l).split()
    colormax = defaultdict(int)
    for count, color in zip(parts[2::2], parts[3::2]):
        colormax[color] = max(colormax[color], int(count))
    total_power += math.prod(colormax.values())

print(total_power)