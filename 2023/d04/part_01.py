import re

with open("input.txt") as f:
    lines = f.readlines()

numbers = [list(map(int, re.findall(r"\d+", line))) for line in lines]
wins = [len(set(n[11:]) & set(n[1:11])) for n in numbers]

total_score = sum(2 ** (w - 1) for w in wins if w > 0)
print(total_score)