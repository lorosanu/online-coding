#!/usr/bin/python3

def areSimilar(a, b):
    if a == b:
        return True

    not_equal = []
    for i in range(len(a)):
        if a[i] != b[i]:
            not_equal.append(a[i])
            not_equal.append(b[i])

    if len(not_equal) > 4:
        return False
    return len(set(not_equal)) <= 2

