with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_6.txt', 'r') as f:
    inp = f.read()

i = 3
while i < len(inp):
    if len(set([inp[i], inp[i-1], inp[i-2], inp[i-3]])) == 4:
        print(i+1)
        break
    i += 1


