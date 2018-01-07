def solution(A):
    left_sum = 0
    right_sum = sum(A)
    
    min_dif = None
    for i in range(1, len(A)):
        left_sum += A[i - 1]
        right_sum -= A[i-1]
        
        print(i, left_sum, right_sum)
        if min_dif is None or abs(left_sum - right_sum) < min_dif:
            min_dif = abs(left_sum - right_sum)
    
    return min_dif


A = [1, 1]
print(A, "=>", solution(A))

A = [0, 0]
print(A, "=>", solution(A))

A = [-1000, 1000]
print(A, "=>", solution(A))

A = [1, 2, 3]
print(A, "=>", solution(A))

A = [3, 1, 2, 4, 3]
print(A, "=>", solution(A))

A = [1, 2, 4, 7, 9, 1000, 23432, 3]
print(A, "=>", solution(A))

A = [43, 543, 8746, 1231, 123, 134, 1, 0]
print(A, "=>", solution(A))
