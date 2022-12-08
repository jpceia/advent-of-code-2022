mat = []

with open('input.txt', 'r') as f:
    for line in f:
        mat.append([int(c) for c in line.strip()])

best_score = 1

for i in range(len(mat)):
    for j in range(len(mat[i])):
        score = 1
        c = mat[i][j]
        # up
        for k in range(1, i + 1):
            if mat[i - k][j] >= c:
                score *= k
                break
        else:
            score *= i
        # down
        for k in range(i+1, len(mat)):
            if mat[k][j] >= c:
                score *= (k - i)
                break
        else:
            score *= (len(mat) - 1 - i)
        # left
        for k in range(1, j + 1):
            if mat[i][j - k] >= c:
                score *= k
                break
        else:
            score *= j
        # right
        for k in range(j+1, len(mat[i])):
            if mat[i][k] >= c:
                score *= (k - j)
                break
        else:
            score *= (len(mat[i]) - 1 - j)

        if score > best_score:
            best_score = score

print(best_score)