n = int(input().strip())

items = set()
occ = {}
for i in range(n):
    number = input().strip()
    items.add(number)
    
    occ[number] = [0 for x in range(10)]    
    for x in range(10):
        occ[number][x] = number.count(str(x))

n = len(items)
numbers = list(items)

g = []   
k = 0
maxs = 0 
for i in range(n):
    check = True
    for j in range(len(g)):
        if i in g[j]:
            check = False
            
    if check:
        g.append([])
        k = len(g) - 1
        g[k].append(i)
        for j in range(i+1, n):
            if occ[numbers[i]] == occ[numbers[j]]:
                g[k].append(j)   
        if len(g[k]) > maxs:
            maxs = len(g[k])

print(len(g))

maxg = [] 
for i in range(len(g)):
    if len(g[i]) == maxs:
        order = []
        for x in g[i]:
            order.append(numbers[x])
        maxg.append(sorted(order, reverse=True))
       
maxg.sort()
for i in range(len(maxg)):
    print(" ".join(maxg[i]))
