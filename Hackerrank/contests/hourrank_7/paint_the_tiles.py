#!/bin/python3

N = int(input().strip())
tiles = input().strip()

nChanges = 1
for i in range(1, len(tiles)):
    if tiles[i] != tiles[i-1]:
        nChanges += 1

print(nChanges)