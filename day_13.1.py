import ast

with open(r'C:\Users\cp\Desktop\AoC-22\inputs\input_13.txt', 'r') as f:
    inp = f.read()

pairs = inp.split("\n\n")

right_order = 0

def check_elem_of_lists(a,b):
    if isinstance(a,int) and isinstance(b,int):
        if a>b:
            return -1
        elif a<b:
            return 1
        else:
            return 0
    elif isinstance(a,list) and isinstance(b,list):
        i = 0
        while i < len(a):
            try:
                temp = check_elem_of_lists(a[i], b[i])
            except:
                return -1
            if temp == 0:
                if i == len(a)-1 and i == len(b) and len(a)!=len(b):
                    return -1
                else:
                    i +=1
            else:
                return temp
        if a == [] and b != []:
            return 1
        elif len(a)< len(b):
            return 1
        else:
            return 0
    elif isinstance(a,list) and isinstance(b,int):
        return check_elem_of_lists(a,[b])
    elif isinstance(a,int) and isinstance(b,list):
        return check_elem_of_lists([a],b)


for item_index, item in enumerate(pairs):
    index = item_index+1
    left = ast.literal_eval(item.splitlines()[0])
    right = ast.literal_eval(item.splitlines()[1])
    ans = check_elem_of_lists(left,right)
    if ans == 1:
        right_order += index
print(right_order)
