#!/usr/bin/python3

def commonCharacterCount(s1, s2):
    sum = 0
    for c in set(s1):
        sum += min(s1.count(c), s2.count(c))
    return sum

