#!/usr/bin/python3

def almostIncreasingSequence(sequence):
    n = len(sequence)
    stack = []
    for i in range(n):
        if len(stack) == 0:
            stack.append(sequence[i])
        elif stack[-1] < sequence[i]:
            stack.append(sequence[i])
        else:
            if i <= n - 2:
                if stack and stack[-1] >= sequence[i + 1]:
                    while stack and stack[-1] >= sequence[i + 1]:
                        stack.pop()
                    if len(stack) == 0 or stack[-1] < sequence[i]:
                        stack.append(sequence[i])
    return (n - len(stack)) <= 1

