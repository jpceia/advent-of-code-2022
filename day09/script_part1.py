lines = []

head_pos = [(0, 0)]
tail_pos = [(0, 0)]

with open('input.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    direction, distance = line[0], int(line[1:])
    for _ in range(distance):
        last_head = head_pos[-1]
        last_tail = tail_pos[-1]
        new_head = list(last_head)
        new_tail = list(last_tail)
        if direction == 'R':
            new_head[0] += 1
            if abs(new_head[0] - last_tail[0]) > 1:
                new_tail = [new_head[0] - 1, new_head[1]]
        elif direction == 'L':
            new_head[0] -= 1
            if abs(new_head[0] - last_tail[0]) > 1:
                new_tail = [new_head[0] + 1, new_head[1]]
        elif direction == 'U':
            new_head[1] += 1
            if abs(new_head[1] - last_tail[1]) > 1:
                new_tail = [new_head[0], new_head[1] - 1]
        elif direction == 'D':
            new_head[1] -= 1
            if abs(new_head[1] - last_tail[1]) > 1:
                new_tail = [new_head[0], new_head[1] + 1]
        head_pos.append(tuple(new_head))
        tail_pos.append(tuple(new_tail))

print(len(set(tail_pos)))
