#!/bin/python3

import sys

n = int(input().strip())
a = [int(x) for x in input().split()]

nt = a.count(1)
if nt % 2 == 1:
    print("No", nt)
else:
    print("Yes", nt)
