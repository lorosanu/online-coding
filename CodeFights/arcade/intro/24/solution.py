#!/usr/bin/python3

def add_elem(matrix, n, m, i, j):
    if i >= 0 and i <= n - 1 and j >= 0 and j <= m - 1:
        return matrix[i][j]
    return False

def minesweeper(matrix):
    n = len(matrix)
    m = len(matrix[0])
    counts = [[0 for i in range(m)] for j in range(n)]
    for i in range(n):
        for j in range(m):
            count = 0
            for p in range(i - 1, i + 2):
                for q in range(j - 1, j + 2):
                    count += add_elem(matrix, n, m, p, q)
            counts[i][j] = count - matrix[i][j]
    return counts

