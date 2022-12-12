lines = []

with open('input.txt', 'r') as f:
    lines = f.readlines()

N = 10
rope = [[(0, 0)] * N]

def update_head(last_head, direction):
    new_head = list(last_head)
    if direction == 'R':
        new_head[0] += 1
    elif direction == 'L':
        new_head[0] -= 1
    elif direction == 'U':
        new_head[1] += 1
    elif direction == 'D':
        new_head[1] -= 1
    return tuple(new_head)

def update_tail(new_head, last_tail):
    new_tail = list(last_tail)
    if new_head[0] > last_tail[0] + 1 and new_head[1] > last_tail[1] + 1:
        new_tail = [new_head[0] - 1, new_head[1] - 1]
    elif new_head[0] > last_tail[0] + 1 and new_head[1] < last_tail[1] - 1:
        new_tail = [new_head[0] - 1, new_head[1] + 1]
    elif new_head[0] < last_tail[0] - 1 and new_head[1] > last_tail[1] + 1:
        new_tail = [new_head[0] + 1, new_head[1] - 1]
    elif new_head[0] < last_tail[0] - 1 and new_head[1] < last_tail[1] - 1:
        new_tail = [new_head[0] + 1, new_head[1] + 1]
    elif new_head[0] > last_tail[0] + 1:
        new_tail = [new_head[0] - 1, new_head[1]]
    elif new_head[0] < last_tail[0] - 1:
        new_tail = [new_head[0] + 1, new_head[1]]
    elif new_head[1] > last_tail[1] + 1:
        new_tail = [new_head[0], new_head[1] - 1]
    elif new_head[1] < last_tail[1] - 1:
        new_tail = [new_head[0], new_head[1] + 1]
    return tuple(new_tail)

for line in lines:
    direction, distance = line[0], int(line[1:])
    for _ in range(distance):
        last_pos = rope[-1]
        new_rope = []
        new_rope.append(update_head(last_pos[0], direction))
        for i in range(1, N):
            new_rope.append(update_tail(new_rope[-1], last_pos[i]))
        rope.append(new_rope)

tail_pos = [pos[-1] for pos in rope]

print(len(set(tail_pos)))
