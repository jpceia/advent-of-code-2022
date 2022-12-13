
import numpy as np

mat = []

alphabet = "abcdefghijklmnopqrstuvwxyz"
start = None
end = None

with open("input.txt", "r") as f:
    for i, line in enumerate(f):
        line = line.strip()
        if not line:
            continue
        row = []
        for j, c in enumerate(line):
            if c == "S":
                start = (i, j)
                c = "a"
            if c == "E":
                end = (i, j)
                c = "z"
            row += [alphabet.index(c)]
        mat.append(row)

vertices = []
edges = {}
dist = {}
prev = {}


for i in range(len(mat)):
    for j in range(len(mat[i])):
        edges[(i, j)] = []
        dist[(i, j)] = float("inf")
        prev[(i, j)] = None

for i in range(len(mat)):
    for j in range(len(mat[i])):
        vertices.append((i, j))
        if i > 0 and (mat[i - 1][j] - mat[i][j] <= 1):
            edges[(i-1, j)].append((i, j))
        if j > 0 and (mat[i][j - 1] - mat[i][j] <= 1):
            edges[(i, j-1)].append((i, j))
        if i < len(mat) - 1 and (mat[i + 1][j] - mat[i][j] <= 1):
            edges[(i+1, j)].append((i, j))
        if j < len(mat[i]) - 1 and (mat[i][j + 1] - mat[i][j] <= 1):
            edges[(i, j+1)].append((i, j))

dist[end] = 0
Q = set(vertices)


while Q:
    u = min(Q, key=lambda x: dist[x])
    Q.remove(u)
    for v in edges[u]:
        alt = dist[u] + 1
        if alt < dist[v]:
            dist[v] = alt
            prev[v] = u


mat = np.array(mat)
sizes = {}

shortest_path = None

for i, j in zip(*np.where(mat == 0)):
    
    S = []
    u = (i, j)
    while u is not None:
        S.insert(0, u)
        u = prev[u]

    if len(S) > 1:
        if shortest_path is None:
            shortest_path = len(S) - 1
        elif len(S) - 1 < shortest_path:
            shortest_path = len(S) - 1

print(shortest_path)