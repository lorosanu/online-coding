def sol(A):
    if len(A) <= 3:
        return 0

    print("A=        ", A)        
    max_end = [0] * len(A)
    for i in range(1, len(A)):
        max_end[i] = max(0, max_end[i-1] + A[i])

    max_start = [0] * len(A)
    for i in range(len(A) - 2, -1, -1):
        max_start[i] = max(0, max_start[i+1] + A[i])

    print("max_start=", max_start)
    print("max_end=  ", max_end)

    maxvalue = 0;
    for i in range(1, len(A) - 1):
        maxvalue = max(maxvalue, max_end[i-1] + max_start[i+1])
        print(i, maxvalue)

    return maxvalue


A = [3, 2, 6, -1, 4, 5, -1, 2]
print(sol(A))
