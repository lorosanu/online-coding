#!/usr/bin/python3

def sortByHeight(a):
    b = sorted(x for x in a if x != -1)
    c = []
    index = 0
    for x in a:
        if x == -1:
            c.append(-1)
        else:
            c.append(b[index])
            index += 1
    return c

