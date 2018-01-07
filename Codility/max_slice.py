def sol(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
        print(a, "=>", max_ending, max_slice)
    return max_slice

A = [5, -7, 3, 5, -2, 4, -1]
print(sol(A))


