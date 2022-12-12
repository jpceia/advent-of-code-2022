import numpy as np

lines = []

with open('input.txt') as f:
    lines = f.readlines()

pos = (0, 0)
pos_steps = []
angle = 90
direction_x = 0
direction_y = 1

mat = np.zeros((100, 10))

for line in lines:
    line = line.split()
    instruction, value = line[0], int(line[1])
    if instruction == 'draai':
        angle += value
        direction_x = int(np.round(np.cos(np.deg2rad(angle))))
        direction_y = int(np.round(np.sin(np.deg2rad(angle))))
    elif instruction == 'loop':
        for k in range(value):
            pos_steps.append((pos[0] + direction_x * (k + 1), pos[1] + direction_y * (k + 1)))
            mat[pos_steps[-1][0] + 90, pos_steps[-1][1]] = 1
        pos = (pos[0] + direction_x * value, pos[1] + direction_y * value)
    elif instruction == 'spring':
        pos = (pos[0] + direction_x * value, pos[1] + direction_y * value)
    else:
        raise ValueError(instruction)
    
for i in range(10):
    row = mat[:, 9 - i]
    print(''.join(['#' if x == 1 else ' ' for x in row][::-1]))