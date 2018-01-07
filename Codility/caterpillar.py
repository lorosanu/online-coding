def caterpillarMethod(A, s):
    n = len(A)
    back, total = 0, 0
    for front in range(n):
        print("front={}, back={}".format(front, back))
        while (back < n and total + A[back] <= s):
            total += A[back]
            back += 1
        print("front={}, back={}, total={}".format(front, back, total))
        if total == s:
            return True
        total -= A[front]
    return False

A = [6, 2, 7, 4, 1, 3, 6]
print(caterpillarMethod(A, 12))
