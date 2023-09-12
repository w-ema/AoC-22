# resolved thanks to https://galaxyinferno.com/how-to-solve-advent-of-code-2022-day-13-with-python/

import ast
with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_13.txt', 'r') as f:
    inp = f.read()

table = [ast.literal_eval(i) for i in inp.splitlines() if i != '']

lower_than_2 = 0
lower_than_6 = 0

def first_value(x):
    if x == []:
        return 0
    else:
        try:
            item = x[0]
            if isinstance(item, int):
                return item
            elif item == []:
                return 0
            elif isinstance(item,list) and len(item) != 0:
                return first_value(item)
            else:
                print(item)
        except:
            print('error', x)


for i in table:
    if first_value(i) < 2:
        lower_than_2 += 1
    if first_value(i) < 6:
        lower_than_6 += 1

print((lower_than_2+1)*(lower_than_6+2))