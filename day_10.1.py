with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_10.txt', 'r') as f:
    inp = f.read()

step = 0
X = 1
signal_strengths = []
for line in inp.splitlines():
    if line == 'noop':
        step += 1
        if step not in [20, 60, 100, 140, 180, 220]:
            pass
        else:
            signal_strengths.append(step*X)
    elif line.split()[0] == 'addx':
        step += 1
        if step not in [20, 60, 100, 140, 180, 220]:
            pass
        else:
            signal_strengths.append(step*X)
        step += 1
        if step not in [20, 60, 100, 140, 180, 220]:
            pass
        else:
            signal_strengths.append(step*X)
        X += int(line.split()[1])

print(sum(signal_strengths))
