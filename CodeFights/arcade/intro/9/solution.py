#!/usr/bin/python3

def allLongestStrings(inputArray):
    m = max(len(x) for x in inputArray)
    return [x for x in inputArray if len(x) == m]

