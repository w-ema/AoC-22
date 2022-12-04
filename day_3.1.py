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

for i in inp[:-1].split("\n"):
    l = len(i)/2
    a = i[:int(l)]
    b = i[int(l):int(2*l)]
    c = []
    for j in a:
        if (j in b) and (j not in c) :
            print(i,j,k[j])
            ans += k[j]
            c.append(j)

print(ans)