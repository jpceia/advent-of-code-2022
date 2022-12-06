result = 0
count = 0

with open("input.txt", "r") as f:
    for line in f:
        count += 1
        line = line.strip()
        part1, part2 = line.split(",")
        i = [int(x) for x in part1.split("-")]
        j = [int(x) for x in part2.split("-")]
        if j[0] >= i[0] and j[0] <= i[1]:
            result += 1
        elif j[1] >= i[0] and j[1] <= i[1]:
            result += 1
        elif j[0] <= i[0] and j[1] >= i[1]:
            result += 1

print("n_lines:", count)
print("result:", result)