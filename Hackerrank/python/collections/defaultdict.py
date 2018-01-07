from collections import defaultdict

with open("input01.txt","r") as rfile:
    n, m = [int(x) for x in rfile.readline().split()]

    a = defaultdict(list)
    for i in range(1, n + 1):
        x = rfile.readline()
        a[x].append(i)

    b = []
    for i in range(1, m + 1):
        x = rfile.readline()
        b.append(x)  

for item in b:
    if item in a:
        print(" ".join(map(str,a[item])))
    else:
        print(-1)
    
