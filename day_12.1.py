# Dijkstra algorithm

from collections import deque
with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_12.txt', 'r') as f:
    inp = f.read()

map = []
for i in inp.splitlines():
    row = []
    for j in i:
        row.append(j)
    map.append(row)

dict = {}

for r in range(len(map)):
    for c in range(len(map[0])):
        if map[r][c] == 'S':
            start = [r,c]
            map[r][c] = 'a'
        elif map[r][c] == 'E':
            end = [r,c]
            map[r][c] = 'z'
        neighbours = []
        for i in [[r-1,c],[r+1,c],[r,c+1],[r,c-1]]:
            if i[0] in range(len(map)) and i[1] in range(len(map[0])):
                if ord(map[i[0]][i[1]]) - ord(map[r][c]) <= 1:
                    neighbours.append(i)
        dict[str([r,c])] = neighbours

q = deque()
q.append((0, start))

vis = [start]

while q:
    d, node = q.popleft()
    for n_node in dict[str(node)]:
        if n_node == end:
            print(d+1)
            quit()
        if n_node in vis:
            continue
        vis.append(n_node)
        q.append((d+1,n_node))