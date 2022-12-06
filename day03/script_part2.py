alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

lines = []

with open("input.txt", "r") as f:
    for line in f:
        lines.append(line)

    for i in range(len(lines) // 3):
        line1 = set(lines[i * 3].strip())
        line2 = set(lines[i * 3 + 1].strip())
        line3 = set(lines[i * 3 + 2].strip())
        el = list(set.intersection(line1, line2, line3))[0]
        res = alphabet.index(el) + 1
        result += res

print(result)