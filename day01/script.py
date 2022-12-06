import numpy as np

calories = [[]]

with open("input.txt") as f:
    for line in f:
        s = line.strip()
        if s:
            calories[-1].append(int(s))
        else:
            calories.append([])

total_cal = [sum(c) for c in calories]

# Part 1
print(max(total_cal))

# Part 2
print(sum(sorted(total_cal, reverse=True)[:3]))