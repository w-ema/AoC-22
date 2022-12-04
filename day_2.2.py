with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_2.txt', 'r') as f:
    inp = f.read()

total = 0
for i in inp[:-1].split('\n'):
    if i[2] == 'Z': #win
        total += 6
        if i[0] == 'A': #you choose paper
            total += 2
        elif i[0] == 'B': #you choose scissors
            total += 3
        else:   #i[0] == 'C' so you choose rock
            total += 1
    elif i[2] == 'Y':   #draw
        total += 3
        if i[0] == 'A':  # you choose rock
            total += 1
        elif i[0] == 'B':  # you choose paper
            total += 2
        else:  # i[0] == 'C' so you choose scissors
            total += 3
    else:   #lose
        if i[0] == 'A':  # you choose scissors
            total += 3
        elif i[0] == 'B':  # you choose rock
            total += 1
        else:  # i[0] == 'C' so you choose paper
            total += 2

print(total)