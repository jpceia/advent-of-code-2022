with open("input.txt", "r") as f:
    s = f.read().strip()

# d = 4 # part 1
d = 14

for i in range(d, len(s)):
    p = s[i - d:i]
    if len(set(p)) == d:
        print(i)
        break
else:
    print("No start-of-packet found")