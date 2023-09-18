with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_15.txt', 'r') as f:
    inp = f.read()

d = {}
x_min = 0
x_max = 0
for line in inp.splitlines():
    x_s = int(line.split()[2][2:-1])
    y_s = int(line.split()[3][2:-1])
    x_b = int(line.split()[8][2:-1])
    y_b = int(line.split()[9][2:])
    r = abs(x_s-x_b)+abs(y_s-y_b)
    d[(x_s, y_s)] = [(x_b, y_b), r]


def number_of_occupied_positions_for_row(y):
    ans = []
    beacons = []
    for k in d:
        if (d[k][0][1] == y) and (d[k][0][1] not in beacons):
            beacons.append(int(d[k][0][0]))
    for k in d:
        if abs(k[1]-y) < d[k][1]:
            x_dist = d[k][1] - abs(k[1]-y)
            for i in range(-x_dist, x_dist+1):
                if k[0]+1 in beacons:
                    pass
                else:
                    ans.append(k[0]+i)
        elif abs(k[1]-y) == d[k][1]:
            if k[0] in beacons:
                pass
            else:
                ans.append(k[0])
    a = set(ans)
    b = set(beacons)
    for i in b:
        if i in a:
            a.remove(i)
    print(len(a))


number_of_occupied_positions_for_row(2000000)