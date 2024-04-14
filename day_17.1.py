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
            return
        else:
            r = rr

def solv(n):
    global h_max
    for i in range(n):
        rock = shapes[int(i) % 5]
        fall(rock)
    return h_max + 1

print(solv(2022))

'''
a=''
for i in range(11,-1,-1):
    for j in range(-2,5):
        if [j,i] in map_of_rocks:
            a += '#'
        else:
            a += '.'
    a += '\n'
print(a)
'''

