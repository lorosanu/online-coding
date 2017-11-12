#!/usr/bin/python3

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    for index, item in enumerate(inputArray):
        if item == elemToReplace:
            inputArray[index] = substitutionElem
    return inputArray

