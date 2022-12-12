mat = []

with open('input.txt', 'r') as f:
    for line in f:
        mat.append([int(c) for c in line.strip()])

result = 0

for i in range(len(mat)):
    for j in range(len(mat[i])):
        c = mat[i][j]
        # up
        for k in range(i):
            if mat[k][j] >= c:
                break
        else:
            result += 1
            continue
        # down
        for k in range(i+1, len(mat)):
            if mat[k][j] >= c:
                break
        else:
            result += 1
            continue
        # left
        for k in range(j):
            if mat[i][k] >= c:
                break
        else:
            result += 1
            continue
        # right
        for k in range(j+1, len(mat[i])):
            if mat[i][k] >= c:
                break
        else:
            result += 1
            continue

print(result)