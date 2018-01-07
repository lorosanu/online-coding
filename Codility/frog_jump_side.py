def solution(X, A):
    path = {}
    
    for i in range(len(A)):
        if A[i] > 0 and A[i] <= X:
            path[A[i]] = 1
        if len(path) == X:
            return i
            
    return -1

print(solution(5, [1]))
print(solution(4, [1, 3, 1, 4, 2, 3, 4]))
print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))
