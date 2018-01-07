def solution(a, n):
    left_sum = 0            # sum(a[:p]) at all times
    right_sum = sum(a)      # sum(a[p+1:]) at all times
    
    for i in range(n):
        right_sum -= a[i]
        if left_sum == right_sum:
            return i
        left_sum += a[i]
        
    return -1

a = [-1, 3, -4, 5, 1, -6, 2, 1]
print(solution(a, len(a)))
