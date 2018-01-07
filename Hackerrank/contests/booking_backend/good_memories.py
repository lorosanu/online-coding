def intersection(a, b):
    return [x for x in a if x in b]

x = int(input().strip())

for i in range(x):
    n = int(input().strip())

    last_pos = -1
    result = "ORDER EXISTS"
    all_destinations = []
    
    for j in range(n):
        c_destinations = input().split(",")
        
        if len(all_destinations) > 0:
            for k in range(len(all_destinations) ):
                i1 = intersection(c_destinations, all_destinations[k])
                i2 = intersection(all_destinations[k], c_destinations)

                if i1 != i2:
                    result = "ORDER VIOLATION"
                    
        all_destinations.append(c_destinations)
        
    print(result)