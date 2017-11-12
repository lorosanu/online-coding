#!/usr/bin/python3

def addBorder(picture):
    wmax = max(len(x) for x in picture) + 2

    border = []
    border.append('*' * wmax)
    for word in picture:
        border.append(word.center(wmax, '*'))
    border.append(border[0])
    return border

