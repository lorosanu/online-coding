n = int(input())

for i in range(1, n): 
    print(sum([i * 10**j for j in range(i)]))

for i in range(1, n): 
    print(sum(map(lambda j: i * 10**j, range(i))))
