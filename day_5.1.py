with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_5.txt', 'r') as f:
    inp = f.read()

stacks = inp.split('\n\n')[0]
rearrangement_procedure = inp.split('\n\n')[1][:-1]

h = len(stacks.split('\n'))
lines = stacks.split("\n")

k={}
j = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
jj = 0
for i in range(1, int(len(lines[0])), 4):
    l = []
    for m in range(h-2, -1, -1):
        if lines[m][i] != ' ':
            l.append(lines[m][i])
    k[j[jj]] = l
    jj += 1

print(rearrangement_procedure)
for i in rearrangement_procedure:




