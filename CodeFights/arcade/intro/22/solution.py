#!/usr/bin/python3

def avoidObstacles(inputArray):
    cmax = max(inputArray)
    jump = 2
    while jump <= cmax:
        multiples = jump
        while multiples <= cmax and multiples not in inputArray:
            multiples += jump
        if multiples > cmax:
            return jump
        jump += 1
    return jump

