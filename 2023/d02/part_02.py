import re, math
from collections import defaultdict

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

total_power = 0
for line in ls:
    parts = re.findall(r'(\d+) (\w+)', line)
    colormax = defaultdict(int)
    for count, color in parts:
        colormax[color] = max(colormax[color], int(count))
    total_power += math.prod(colormax.values())

print(total_power)
