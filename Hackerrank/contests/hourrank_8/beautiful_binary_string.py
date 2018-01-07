#!/bin/python3

import sys

n = int(input().strip())
B = input().strip()

i = 2
count = 0
while i < n:
    if B[i-2:i+1] == "010":
        count += 1
        i += 2
    i += 1
   
print(count)