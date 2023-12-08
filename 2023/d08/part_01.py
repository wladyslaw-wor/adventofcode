import re
from itertools import cycle

with open("input.txt") as f:
    ws = [re.findall("\w+", l) for l in f.read().strip().split("\n")]

(dirs, ), _, *moves = ws
move = {
    "L": {start: l for start, l, _ in moves},
    "R": {start: r for start, _, r in moves},
}

def length(here, part1=False):
    for i, d in enumerate(cycle(dirs)):
        here = move[d][here]
        if (part1 and here == "ZZZ") or (not part1 and here[-1] == "Z"):
            return i + 1

print(length("AAA", part1=True))