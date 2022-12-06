alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = 0

with open("input.txt", "r") as f:
    for line in f:
        line = line.strip()
        n = len(line)
        s1 = set(line[:int(n/2)])
        s2 = set(line[int(n/2):])
        el = list(set.intersection(s1, s2))[0]
        res = alphabet.index(el) + 1
        result += res

print(result)