def solution(a, n):
    left_sum = [0 for i in range(n)]
    right_sum = [0 for i in range(n)]

    for i in range(1, n):
        left_sum[i] = left_sum[i-1] + a[i-1]

    for i in range(n-2, -1, -1):
        right_sum[i] = right_sum[i+1] + a[i+1]

    for i in range(0, n):
        if left_sum[i] == right_sum[i]:
            return i        
        
    return -1

a = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(a, len(a)))
