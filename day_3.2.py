import string
with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_3.txt', 'r') as f:
    inp = f.read()

ans = 0
k = {}

j = 1
for i in string.ascii_lowercase:
    k[i] = j
    j +=1
j = 27
for i in string.ascii_uppercase:
    k[i] = j
    j +=1

number_of_lines = len(inp[:-1].split("\n"))
x = int(number_of_lines/3)
y = inp[:-1].split("\n")

for i in range(x):
    a = y[3*i]
    b = y[3*i+1]
    c = y[3*i+2]
    d = []
    for j in a:
        if j in b and j in c and j not in d:
            ans += k[j]
            d.append(j)

print(ans)