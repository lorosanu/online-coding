#!/usr/bin/python3

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    strongest = max([yourLeft, yourRight]) == max([friendsLeft, friendsRight])
    weakest = min([yourLeft, yourRight]) == min([friendsLeft, friendsRight])
    return strongest and weakest

