def solution(X, Y, D):
    steps = (Y - X) // D
    if (Y - X) % D == 0:
        return steps
    else:
        return steps + 1


print(solution(1, 1, 3))
print(solution(1, 3, 1))
print(solution(1, 5, 3))
