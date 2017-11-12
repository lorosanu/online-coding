#!/usr/bin/python3

def makeArrayConsecutive2(statues):
    s = [0] * 20
    for x in statues:
        s[x] = 1
    return s[min(statues):max(statues)+1].count(0)

