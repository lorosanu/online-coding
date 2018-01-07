def solution_v2(A):
    unique = {}
    for x in A:
        if x in unique:
            del unique[x]
        else:
            unique[x] = 1
    for x in unique:
        return x

def solution(A):
    sol = A[0]
    print(0, sol)
    for i in range(1, len(A)):        
        sol = sol ^ A[i]
        print(i, sol)
    return sol


A = [9, 3, 5, 7, 9, 3, 9, 7, 9]
print(A)
print(solution(A))
