def solution(A, K):
    if len(A):
        K = K % len(A)
        for i in range(K):
            x = A.pop()
            A.insert(0, x)
    return A


A = [3, 8, 9, 7, 6]
K = 0
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 1
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 2
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 3
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 4
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 5
print(solution(A, K))

A = [3, 8, 9, 7, 6]
K = 6
print(solution(A, K))

A = [1]
K = 6
print(solution(A, K))

A = [1, 2]
K = 5
print(solution(A, K))

A = [1, 2, 3]
K = 5
print(solution(A, K))

A = []
K = 5
print(solution(A, K))


