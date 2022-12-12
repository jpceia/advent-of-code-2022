x = [1]

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            x.append(x[-1])
        elif line[:4] == "addx":
            x.append(x[-1])
            x.append(x[-1] + int(line[5:]))
        else:
            raise ValueError

steps = [20, 60, 100, 140, 180, 220]

total = 0
for i in steps:
    total += x[i - 1] * i

print(total)