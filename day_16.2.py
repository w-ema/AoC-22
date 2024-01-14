# the solution takes quite a long time ~15min !!! but it works xD
from functools import cache
import re

with open(r'inputs\input_16.txt', 'r') as f:
    inp = f.read()

d = {}
pattern = "Valve ([A-Z]+) has flow rate=([0-9]+); tunnel(|s) lead(|s) to valve(|s) ([A-Z, ]+)"

for line in inp.splitlines():
    valve = re.search(pattern, line).group(1)
    flow_rate = int(re.search(pattern, line).group(2))
    neighbours = re.search(pattern, line).group(6)
    d[valve] = [flow_rate, [x for x in neighbours.split(", ")]]


valuable_valves = [x for x in d.keys() if d[x][0] != 0]


@cache
def solve(valve, time, opened, z):
    if time == 0:
        if z-1 > 0:
            z -= 1
            return solve('AA', 26, opened, z)
        return 0

    score = max(solve(n,time-1,opened,z) for n in d[valve][1])

    if valve in valuable_valves and valve not in opened:
        new_opened = set(opened)
        new_opened.add(valve)
        score = max(score, (time-1)*d[valve][0] + solve(valve, time-1, frozenset(new_opened),z))

    return score


print(solve('AA', 26, frozenset(), 2))
