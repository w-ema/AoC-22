with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_6.txt', 'r') as f:
    inp = f.read()

i = 13
while i < len(inp):
    if len(set(inp[i-13:i+1])) == 14:
        print(i+1)
        break
    i += 1