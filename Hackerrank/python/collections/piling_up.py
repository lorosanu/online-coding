from collections import deque

k = int(input().strip())

for i in range(k):
    n = int(input().strip())
    cubes = deque([int(x) for x in input().split()])
    
    j = 0
    cube = 2**31
    stack = True
    while j < len(cubes) and stack :
        if cubes[0] >= cubes[-1]:
            if cubes[0] <= cube:
                cube = cubes.popleft()
            else:
                stack = False
        else:
            if cubes[-1] <= cube:
                cube = cubes.pop()        
            else:
                stack = False
            
    if stack:
        print("Yes")
    else:
        print("No")

        
        
    
