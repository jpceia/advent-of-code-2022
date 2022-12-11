with open("input.txt") as f:
    content = f.readlines()

monkeys = []

for i in range(8):
    monkey = {}
    monkey['items'] = [int(i) for i in content[i * 7 + 1][18:].split(', ')]
    monkey['op'] = content[i * 7 + 2][19:].strip()
    monkey['div'] = int(content[i * 7 + 3][21:])
    monkey['true'] = int(content[i * 7 + 4][29:])
    monkey['false'] = int(content[i * 7 + 5][29:])
    monkey['inspections'] = 0
    monkeys.append(monkey)

for _ in range(20):
    for k, monkey in enumerate(monkeys):
        for item in monkey['items']:
            monkey['inspections'] += 1
            old = item
            worry = eval(monkey['op'])
            worry = worry // 3
            if worry % monkey['div'] == 0:
                monkeys[monkey['true']]['items'].append(worry)
            else:
                monkeys[monkey['false']]['items'].append(worry)
        monkey['items'] = []

for monkey in monkeys:
    print(monkey['inspections'])