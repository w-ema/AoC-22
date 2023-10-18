# finally thanks to https://www.youtube.com/watch?v=pV5nNyjMdFA

with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_15.txt', 'r') as f:
    inp = f.read()

d = {}

for line in inp.splitlines():
    x_s = int(line.split()[2][2:-1])
    y_s = int(line.split()[3][2:-1])
    x_b = int(line.split()[8][2:-1])
    y_b = int(line.split()[9][2:])
    r = abs(x_s-x_b)+abs(y_s-y_b)
    d[(x_s, y_s)] = [(x_b, y_b), r]

all_possible_positions = set()

def check_point(i):
    for k in d:
        if abs(k[0]-i[0])+abs(k[1]-i[1])<=d[k][1]:
            return False
    return True

for k in d:
    for dx in range(d[k][1]+2):
        dy = d[k][1] + 1 - dx
        for x,y in [(k[0]-dx,k[1]-dy),(k[0]-dx,k[1]+dy),(k[0]+dx,k[1]-dy),(k[0]+dx,k[1]+dy)]:
            if not (0<=x<=4000000 and 0<=y<=4000000):
                continue
            if check_point((x,y)):
                print(4000000*x+y)
                exit()
