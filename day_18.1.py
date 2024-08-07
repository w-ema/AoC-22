with open(r'inputs\input_18.txt', 'r') as f:
    inp = f.read()

d = []
for i in inp.splitlines():
    x,y,z = i.split(',')
    d.append([int(x),int(y),int(z)])

total = 0
for i in d:
    x, y, z = i
    s = 6
    for j in [[x-1,y,z],[x+1,y,z],[x,y-1,z],[x,y+1,z],[x,y,z-1],[x,y,z+1]]:
        if j in d:
            s -= 1
    total += s

print(total)

