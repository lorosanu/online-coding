#!/usr/bin/python3

def distance(a, b):
    diff = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            diff += 1
    return diff == 1

def check_paths(c, n):
    for i in range(n):
        visited = [[False for _ in range(n)] for _ in range(n)]
        stack = [i]
        while len(stack) > 0:
            top = stack[-1]
            level_up = False
            for j in c[top]:
                if not visited[top][j] and not j in stack:
                    stack.append(j)
                    visited[top][j] = True
                    level_up = True
                    break
            if not level_up:
                p = stack.pop()
                for i in range(n):
                    visited[p][i] = False
            if len(stack) == n:
                return True
    return False

def stringsRearrangement(inputArray):
    n = len(inputArray)
    c = dict([i, []] for i in range(n))
    for i in range(n):
        for j in range(n):
            if distance(inputArray[i], inputArray[j]):
                c[i].append(j)
    if [] in c.values():
        return False
    return check_paths(c, n)

