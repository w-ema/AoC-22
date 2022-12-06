with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_4.txt', 'r') as f:
    inp = f.read()

ans = 0

for i in inp.split("\n")[:-1]:
    a, b = i.split(',')[0], i.split(',')[1]
    first_elf = [i for i in range(int(a.split('-')[0]), int(a.split('-')[1])+1)]
    second_elf = [i for i in range(int(b.split('-')[0]), int(b.split('-')[1])+1)]
    if len(first_elf) <= len(second_elf):
        if first_elf[0] >= second_elf[0] and first_elf[-1] <= second_elf[-1]:
            ans += 1
    else:
        if second_elf[0] >= first_elf[0] and second_elf[-1] <= first_elf[-1]:
            ans += 1

print(ans)