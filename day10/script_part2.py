x = 1
data = ['#']

clock = 0
with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        if line == "noop":
            if abs(len(data) % 40 - x) < 2:
                data.append('#')
            else:
                data.append('.')
        elif line[:4] == "addx":
            if abs(len(data) % 40 - x) < 2:
                data.append('#')
            else:
                data.append('.')
            x += int(line[5:])
            if abs(len(data) % 40 - x) < 2:
                data.append('#')
            else:
                data.append('.')
        else:
            raise ValueError

for i in range(6):
    print(''.join(data[i * 40:][:40]))