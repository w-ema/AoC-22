with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_14.txt','r') as f:
    inp = f.read()

source = (500,0)
r = []
s = []

x_max = 500
x_min = 500
y_max = 0

for path in inp.splitlines():
    lines = path.split(' -> ')
    r_temp = []
    for l in range(1,len(lines)):
        line_1 = lines[l-1].split(',')
        line_2 = lines[l].split(',')
        if line_1[0] == line_2[0]:
            x = int(line_1[0])
            if x > x_max:
                x_max = x
            elif x < x_min:
                x_min = x
            for y in range(min(int(line_1[1]),int(line_2[1])),max(int(line_1[1]),int(line_2[1]))+1):
                if (x,y) not in r_temp:
                    r_temp.append((x,y))
                if y > y_max:
                    y_max = y
        elif line_1[1] == line_2[1]:
            y = int(line_1[1])
            if y > y_max:
                y_max = y
            for x in range(min(int(line_1[0]), int(line_2[0])), max(int(line_1[0]), int(line_2[0])) + 1):
                if (x, y) not in r_temp:
                    r_temp.append((x, y))
                if x > x_max:
                    x_max = x
                elif x < x_min:
                    x_min = x
    r += r_temp
set_of_r = set(r)

number_of_units = 0
sand = [source[0], source[1]]
while sand[1] <= y_max:
    if (sand[0],sand[1]+1) in set_of_r:
        #print('pod spodem skała')
        if (sand[0]-1, sand[1]+1) in set_of_r:
            #print('po prawej skała')
            if (sand[0]+1, sand[1]+1) in set_of_r:
                #print('po lewej skała')
                #print('piasek zostaje w ',(sand[0],sand[1]))
                s = (sand[0], sand[1])
                set_of_r.update([s])
                number_of_units += 1
                #print(set_of_r)
                sand = [source[0],source[1]]
            else:
                sand[0] += 1
                sand[1] += 1
        else:
            sand[0] -= 1
            sand[1] += 1
    else:
        sand[1] += 1

print(number_of_units)