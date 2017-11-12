#!/usr/bin/python3

def isLucky(n):
    a = [int(c) for c in str(n)]
    middle = len(a) // 2
    return sum(a[0:middle]) == sum(a[middle:])

