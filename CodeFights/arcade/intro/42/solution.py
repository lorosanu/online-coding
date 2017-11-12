#!/usr/bin/python3

def bishopAndPawn(bishop, pawn):
    distl = abs(ord(bishop[0]) - ord(pawn[0]))
    distd = abs(int(bishop[1]) - int(pawn[1]))
    return distl == distd
