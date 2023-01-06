# the solution comes from https://www.youtube.com/watch?v=FXQWIWHaFBE

with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_7.txt', 'r') as f:
    inp = f.read()

dict = {'/home': 0}
path = '/home'

for i in inp.splitlines()[1::]:
    if i[0] == '$':
        if i[2:4] == 'cd':
            if i[5:6] == '/':
                path = '/home'
            elif i[5:7] == '..':
                path = path[:path.rfind("/")]
            else:
                path += '/' + str(i.split()[2])
                dict.update({path: 0})
        else:
            pass
    elif i[:3] == 'dir':
        pass
    else:
        size = int(i.split()[0])
        dir = path
        for i in range(path.count('/')):
            dict[dir] += size
            dir = dir[:dir.rfind('/')]

total = 0
for dir in dict:
    total += dict[dir]

used = dict['/home']
needed_to_delete = used - 40000000

file_enough = []
for dir in dict:
    if dict[dir] >= needed_to_delete:
        file_enough.append(dict[dir])

print(min(file_enough))
