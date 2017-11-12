#!/usr/bin/python3

def alphabeticShift(inputString):
    letters_from = string.ascii_lowercase
    letters_to = letters_from[1:] + letters_from[0]
    change = str.maketrans(letters_from, letters_to)
    return inputString.translate(change)

