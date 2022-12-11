import numpy as np

lines = []

with open('input.txt') as f:
    lines = f.readlines()

pos = (0, 0)
angle = 90
direction_x = 0
direction_y = 1

for line in lines:
    line = line.split()
    instruction, value = line[0], int(line[1])
    if instruction == 'draai':
        angle += value
        direction_x = int(np.round(np.cos(np.deg2rad(angle))))
        direction_y = int(np.round(np.sin(np.deg2rad(angle))))
    elif instruction == 'loop':
        pos = (pos[0] + direction_x * value, pos[1] + direction_y * value)
    elif instruction == 'spring':
        pos = (pos[0] + direction_x * value, pos[1] + direction_y * value)
    else:
        raise ValueError(instruction)
    
    print(pos)