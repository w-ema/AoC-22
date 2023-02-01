with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_9.txt', 'r') as f:
    inp = f.read()

T_position = [(0,0)]
t_x = 0
t_y = 0
h_x = 0
h_y = 0

def tMover(t_x, t_y, h_x, h_y):
    if t_x == h_x and t_y == h_y:
        pass
    elif (abs(t_x - h_x) == 1 and t_y == h_y) or (abs(t_y - h_y) == 1 and t_x == h_x):
        pass
    elif abs(t_x - h_x) == 1 and abs(t_y - h_y) == 1:
        pass
    elif t_y == h_y and abs(t_x - h_x) == 2:
        if t_x - h_x == 2:
            t_x -= 1
        else:
            t_x += 1
    elif t_x == h_x and abs(t_y - h_y) == 2:
        if t_y - h_y == 2:
            t_y -= 1
        else:
            t_y += 1
    elif abs(t_x - h_x) == 1 and abs(t_y - h_y) == 2:
        t_x = h_x
        if t_y - h_y == 2:
            t_y -= 1
        else:
            t_y += 1
    elif abs(t_y - h_y) == 1 and abs(t_x - h_x) == 2:
        t_y = h_y
        if t_x - h_x == 2:
            t_x -= 1
        else:
            t_x += 1
    if (t_x, t_y) not in T_position:
        T_position.append((t_x,t_y))
    return t_x, t_y


for line in inp.splitlines():
    for move in range(int(line.split()[1])):
        if line.split()[0] == 'U':
            h_y += 1
        elif line.split()[0] == 'D':
            h_y -= 1
        elif line.split()[0] == 'R':
            h_x += 1
        elif line.split()[0] == 'L':
            h_x -= 1
        print(line)
        print('h:', h_x, h_y)
        t_x, t_y = tMover(t_x, t_y, h_x, h_y)
        print('t:', t_x, t_y)


print("The score: ",len(T_position))