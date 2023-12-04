import itertools, re

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

box = list(itertools.product((-1, 0, 1), repeat=2))
parts_by_symbol = {(i, j): (x, []) for i, l in enumerate(ls) for j, x in enumerate(l) if x != "." and not x.isdigit()}

part_sum = 0

for i, l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group(0))
        boundary = {(i + di, j + dj) for di, dj in box for j in range(match.start(), match.end())}
        if parts := parts_by_symbol.keys() & boundary:
            part_sum += n

print(part_sum)
