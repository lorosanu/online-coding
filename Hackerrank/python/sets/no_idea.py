n, m = input().split()
n = int(n)
m = int(m)

array = {}
for x in input().split():
    x = int(x)
    if x not in array:
        array[x] = 1
    else:
        array[x] += 1

A = set([int(x) for x in input().split()])
B = set([int(x) for x in input().split()])                   

n_happy = 0
for x in A:    
    if x in array:
        n_happy += array[x]
        
n_sad = 0
for x in B:
    if x in array:
        n_sad += array[x]
        
print(n_happy - n_sad)