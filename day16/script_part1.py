import numpy as np

valves_list = []
data = []

with open("input.txt", "r") as f:
    for line in f:
        part1, part2 = line.strip().split("; ")
        valve = part1.split()[1]
        flow_rate = part1.split("=")[1]
        next_valves = part2[23:].split(", ")
        print(valve, flow_rate, next_valves)
        if valve in valves_list:
            pass
        else:
            valves_list.append(valve)
        for v in next_valves:
            if v in valves_list:
                pass
            else:
                valves_list.append(v)
        data.append({
            "valve": valves_list.index(valve),
            "flow_rate": int(flow_rate),
            "next_valves": [valves_list.index(v) for v in next_valves]
        })

N = len(valves_list)
T = 30
rates = np.zeros(N, dtype=np.int32)
for d in data:
    rates[d["valve"]] = d["flow_rate"]
mat = np.zeros((N, N), dtype=np.int32)
for d in data:
    for v in d["next_valves"]:
        mat[d["valve"]][v] = 1

# start at 0
# sort items by flow rate
# max flow rate = 0
start = 0