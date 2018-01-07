from itertools import product

k, m = [int(x) for x in input().split()]

rlist = []
for i in range(k):
    a = [int(x) for x in input().split()]
    rlist.append(a[1:])

plist = list(product(*rlist))

max_sum = 0
for combination in plist:
    csum = sum([x**2 for x in combination]) % m
    if csum > max_sum :
        max_sum = csum 
     
print(max_sum)
