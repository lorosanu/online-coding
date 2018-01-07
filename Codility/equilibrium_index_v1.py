def solution(a, n):
    for i in range(0, n):
        left_sum = 0
        right_sum = 0
        
        for j in range(0, i):
            left_sum += a[j]

        for j in range(i+1, n):
            right_sum += a[j]

        if left_sum == right_sum:
            return i
    return -1

a = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(a, len(a)))
