#!/bin/python3

n, m = [ int(x) for x in input().split() ]

if m < n:
    print(n - m)
elif m % n == 0:
    print(0)
else:
    print(n - m % n)
