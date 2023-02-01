with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_9.txt', 'r') as f:
    inp = f.read()

T9_position = [(0,0)]
t1_x, t2_x, t3_x, t4_x, t5_x, t6_x, t7_x, t8_x, t9_x = 0, 0, 0, 0, 0, 0, 0, 0, 0
t1_y, t2_y, t3_y, t4_y, t5_y, t6_y, t7_y, t8_y, t9_y = 0, 0, 0, 0, 0, 0, 0, 0, 0
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
    elif abs(t_y - h_y) == 2 and abs(t_x - h_x) == 2:
        if h_x - t_x == 2:
            t_x += 1
            if h_y - t_y == 2:
                t_y += 1
            else:
                t_y -= 1
        else:
            t_x -= 1
            if h_y - t_y == 2:
                t_y += 1
            else:
                t_y -= 1
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
        t1_x, t1_y = tMover(t1_x, t1_y, h_x, h_y)
        t2_x, t2_y = tMover(t2_x, t2_y, t1_x, t1_y)
        t3_x, t3_y = tMover(t3_x, t3_y, t2_x, t2_y)
        t4_x, t4_y = tMover(t4_x, t4_y, t3_x, t3_y)
        t5_x, t5_y = tMover(t5_x, t5_y, t4_x, t4_y)
        t6_x, t6_y = tMover(t6_x, t6_y, t5_x, t5_y)
        t7_x, t7_y = tMover(t7_x, t7_y, t6_x, t6_y)
        t8_x, t8_y = tMover(t8_x, t8_y, t7_x, t7_y)
        t9_x, t9_y = tMover(t9_x, t9_y, t8_x, t8_y)
        if (t9_x, t9_y) not in T9_position:
            T9_position.append((t9_x, t9_y))


print("The score: ",len(T9_position))