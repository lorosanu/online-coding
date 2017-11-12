#!/usr/bin/python3

def arrayMaxConsecutiveSum(inputArray, k):
    n = len(inputArray)

    sums = [0 for i in range(n)]
    sums[0] = inputArray[0]
    for i in range(1, n):
        sums[i] = sums[i-1] + inputArray[i]

    smax = sums[0]
    for i in range(n - k):
        sc = sums[i+k] - sums[i]
        if sc > smax:
            smax = sc
    return smax

