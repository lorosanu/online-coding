#!/usr/bin/python3

def adjacentElementsProduct(inputArray):
    p = -1000000
    for i in range(len(inputArray) - 1):
        cp = inputArray[i] * inputArray[i + 1]
        if cp > p:
            p = cp
    return p

