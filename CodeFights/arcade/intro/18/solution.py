#!/usr/bin/python3

def palindromeRearranging(inputString):
    counts = {}
    for s in inputString:
        if s in counts:
            counts[s] += 1
        else:
            counts[s] = 1
    odd_counts = [x for x in counts.values() if x % 2 == 1]
    return len(odd_counts) <= 1

