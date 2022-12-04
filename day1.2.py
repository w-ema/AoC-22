with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_1.txt', 'r') as f:
    inp = f.read()

elves_list = inp[:-1].split('\n\n')
elves_calories = [i.split('\n') for i in elves_list]
total_calories_for_each_elf = []

for i in elves_calories:
    t = 0
    for j in i:
        t += int(j)
    total_calories_for_each_elf.append(t)

total_calories_for_each_elf.sort()
print(total_calories_for_each_elf[-3:])
sum_of_three = sum(total_calories_for_each_elf[-3:])
print(sum_of_three)
