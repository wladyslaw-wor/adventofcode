import itertools
import math
import re

with open("input.txt") as f:
    ls = f.read().strip().split("\n")

box = list(itertools.product((-1, 0, 1), (-1, 0, 1)))
parts_by_symbol = {
    (i, j): (x, [])
    for i, l in enumerate(ls)
    for j, x in enumerate(l)
    if x != "." and not x.isdigit()
}

for i, l in enumerate(ls):
    for match in re.finditer(r"\d+", l):
        n = int(match.group(0))
        boundary = {
            (i + di, j + dj)
            for di, dj in box
            for j in range(match.start(), match.end())
        }
        for symbol in parts_by_symbol.keys() & boundary:
            parts_by_symbol[symbol][1].append(n)

print(
    sum(
        math.prod(parts)
        for symbol, parts in parts_by_symbol.values()
        if len(parts) == 2 and symbol == "*"
    )
)