#!/usr/bin/python3

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if value1 >= value2 or weight2 > maxW:
        if weight1 <= maxW:
            return value1
    else:
        if weight2 <= maxW:
            return value2
    return 0

