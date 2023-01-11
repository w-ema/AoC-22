with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_8.txt', 'r') as f:
    inp = f.read()

table = [[int(r[c]) for c in range(len(r))] for r in inp.splitlines()]
width = len(table[0])
hight = len(table)
all_scores = []

for i in range(1,hight-1):
    for j in range(1,width-1):
        u = 0
        d = 0
        l = 0
        r = 0
        for k in range(j-1, -1, -1):
            if table[i][k] < table[i][j]:
                l += 1
            elif table[i][k] >= table[i][j]:
                l += 1
                break
            else:
                break
        for k in range(j+1, width):
            if table[i][k] < table[i][j]:
                r += 1
            elif table[i][k] >= table[i][j]:
                r += 1
                break
            else:
                break
        for k in range(i-1, -1, -1):
            if table[k][j] < table[i][j]:
                u += 1
            else:
                u += 1
                break
        for k in range(i+1, hight):
            if table[k][j] < table[i][j]:
                d += 1
            elif table[k][j] >= table[i][j]:
                d += 1
                break
            else:
                break
        all_scores.append(u*d*r*l)

print(max(all_scores))
