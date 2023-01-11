with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_8.txt', 'r') as f:
    inp = f.read()

table = [[int(r[c]) for c in range(len(r))] for r in inp.splitlines()]
width = len(table[0])
hight = len(table)
total = 2*width + 2*hight - 4

for i in range(1,hight-1):
    for j in range(1,width-1):
        if all(table[i][j] > table[i][k] for k in range(0, j)) or all(table[i][j] > table[i][k] for k in range(j+1, width)) or all(table[i][j] > table[k][j] for k in range(0, i)) or all(table[i][j] > table[k][j] for k in range(i+1, hight)):
            total += 1

print(total)
