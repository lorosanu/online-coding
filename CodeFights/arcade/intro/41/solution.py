#!/usr/bin/python3

def sum_digits(n):
    return sum(int(x) for x in list(str(n)))

def digitDegree(n):
    degree = 0
    while n >= 10:
        n = sum_digits(n)
        degree += 1
    return degree

