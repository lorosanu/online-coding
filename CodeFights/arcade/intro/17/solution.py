#!/usr/bin/python3

def arrayChange(a):
    moves = 0
    for i in range(1, len(a)):
        if a[i] <= a[i - 1]:
            moves += a[i - 1] - a[i] + 1
            a[i] = a[i - 1] + 1
    return moves

