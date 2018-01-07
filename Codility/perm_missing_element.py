def solution(A):
    if len(A) == 0:
        return 1
        
    n = len(A) + 1
    sum_total = n * (n + 1) / 2
    sum_given = sum(A)
    
    return sum_total - sum_given

print(solution([]))
print(solution([1]))
print(solution([2]))
print(solution([1, 3]))
print(solution([5, 2, 4, 3]))
