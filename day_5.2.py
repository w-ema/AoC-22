with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_5.txt', 'r') as f:
    inp = f.read()

stacks = inp.split('\n\n')[0]
rearrangement_procedure = inp.split('\n\n')[1].split('\n')[:-1]

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

for i in rearrangement_procedure:
    numbers_of_steps = i.split()[1]
    present_stack = i.split()[3]
    destination_stack = i.split()[5]
    moved_crate = k[present_stack][-int(numbers_of_steps):]
    print(numbers_of_steps, moved_crate)
    for j in moved_crate:
        k[destination_stack].append(j)
    del k[present_stack][-int(numbers_of_steps):]

ans = ''
for i in k.keys():
    ans += str(k[i][-1])
print(ans)
