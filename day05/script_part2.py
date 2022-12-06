

with open("input.txt", "r") as f:
    lines = f.readlines()

crates = []
for k in range(9):
    crate = []
    for i in [7, 6, 5, 4, 3, 2, 1, 0]:
        box = lines[i][4 * k + 1].strip()
        if not box:
            break
        crate.append(box)
    crates.append(crate)

moves = []
for line in lines[10:]:
    tmp = line.split()
    data = [
        int(tmp[1]),
        int(tmp[3]) - 1,
        int(tmp[5]) - 1,
    ]
    moves.append(data)

# Apply moves
for move in moves:
    qty = move[0]
    from_crate = crates[move[1]]
    to_crate = crates[move[2]]

    for k in range(qty):
        to_crate.append(from_crate[k - qty])
    for _ in range(qty):
        from_crate.pop()

for crate in crates:
    print(crate[-1], end='')
print()