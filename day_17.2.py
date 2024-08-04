with open(r'inputs\input_17.txt', 'r') as f:
    inp = f.read()


shapes = [[[0,0],[1,0],[2,0],[3,0]],
          [[1,0],[0,1],[1,1],[2,1],[1,2]],
          [[0,0],[1,0],[2,0],[2,1],[2,2]],
          [[0,0],[0,1],[0,2],[0,3]],
          [[0,0],[1,0],[0,1],[1,1]]]

h_max = -1
map_of_rocks = []
jet_pattern = inp
ind_jet_pattern = 0
repeater = 0
d = {}

def beginning_position(x):
    y = []
    for i in range(len(x)):
        y.append([x[i][0], x[i][1] + h_max + 4])
    return y


def right_or_left_move(r):
    global ind_jet_pattern
    direction = jet_pattern[ind_jet_pattern]
    new_r = []
    for i in r:
        if direction == "<":
            new_r.append([i[0] - 1, i[1]])
        elif direction == ">":
            new_r.append([i[0] + 1, i[1]])
    if ind_jet_pattern < len(jet_pattern)-1:
        ind_jet_pattern += 1
    else:
        ind_jet_pattern = 0
    if any([new_r[i][0]<-2 for i in range(len(new_r))]) or any([new_r[i][0]>4 for i in range(len(new_r))]) or any([new_r[i] in map_of_rocks for i in range(len(new_r))]):
        return r
    else:
        return new_r

def fall_down(r):
    new_r = []
    for i in r:
        new_r.append([i[0], i[1] - 1])
    if any([new_r[i][1] == -1 for i in range(len(new_r))]) or any([new_r[i] in map_of_rocks for i in range(len(new_r))]):
        map_of_rocks.extend(r)
        return r
    else:
        return new_r


def fall(x):
    global h_max
    r = beginning_position(x)
    r_is_moved = True
    while r_is_moved:
        r = right_or_left_move(r)
        rr = fall_down(r)
        if r == rr:
            h_r = max([r[i][1] for i in range(len(r))])
            if h_max < h_r:
                h_max = h_r
            return r
        else:
            r = rr

def solv(n):
    global h_max
    global repeater
    global ind_jet_pattern
    visited = []
    ir = 0
    hr = 0
    r = 0
    for i in range(n):
        rock = shapes[i%5]
        rock_pos = fall(rock)
        d[i] = [ind_jet_pattern, h_max + 1, rock_pos]
        visited.append([rock_pos[i][0] for i in range(len(rock_pos))])
        if i > 2022:
            for j in range(len(visited)-2,0,-1):
                if visited[i] == visited[j]:
                    if d[i][0] == d[j][0] and i%5 == j%5:
                        ir = i-j
                        hr = d[i][1] - d[j][1]
                        for s in range(5):
                            if d[i-s][1] - d[j-s][1] == hr and d[i-s][0] == d[j-s][0]:
                                r += 1
                        if r == 5:
                            return ((n-j)//ir)*hr + d[((n-j)%ir)+j][1] -1
    return h_max + 1

print(solv(1000000000000))