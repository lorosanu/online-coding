#!/usr/bin/python3

def arrayMaximalAdjacentDifference(v):
    max_diff = abs(v[0] - v[1])
    for i in range(len(v) - 1):
        diff = abs(v[i] - v[i + 1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

