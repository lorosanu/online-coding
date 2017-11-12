#!/usr/bin/python3

def longestDigitsPrefix(inputString):
    i = 0
    n = len(inputString)
    while  i < n and inputString[i].isdigit():
        i += 1
    return inputString[:i]

