with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_10.txt', 'r') as f:
    inp = f.read()

step = 0
steps = {0:1}
X = 1
for line in inp.splitlines()[:-1]:
    if line == 'noop':
        step += 1
        if step not in steps.keys():
            steps[step] = X
    elif line.split()[0] == 'addx':
        step += 1
        if step not in steps.keys():
            steps[step] = X
        step += 1
        X += int(line.split()[1])
        if step not in steps.keys():
            steps[step] = X


ans = ''
for s in steps:
    if s%40 in [steps.get(s,-10)-1, steps.get(s,-10), steps.get(s,-10)+1]:
        add = 'X'
    else:
        add = '.'
    if s%40 == 0:
        ans += '\n' + add
    else:
        ans += add
print(ans)
