with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_2.txt', 'r') as f:
    inp = f.read()

total = 0
for i in inp[:-1].split('\n'):
    if i[2] == 'X': #rock is your choice
        total += 1
        if i[0] == 'A': #draw
            total += 3
        elif i[0] == 'C': #win
            total += 6
    elif i[2] == 'Y':   #paper is your choice
        total += 2
        if i[0] == 'B':  # draw
            total += 3
        elif i[0] == 'A':  # win
            total += 6
    else:   #scissors is your choice
        total += 3
        if i[0] == 'C':  # draw
            total += 3
        elif i[0] == 'B':  # win
            total += 6

print(total)