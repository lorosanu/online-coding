#!/usr/bin/py

def stringReduction(a):   
    countA = a.count('a')
    countB = a.count('b')
    countC = a.count('c')
    if countA == len(a) or countB == len(a) or countC == len(a):
        return len(a)
    if countA % 2 == 0 and countB % 2 == 0 and countC % 2 == 0:
        return 2
    if countA % 2 == 1 and countB % 2 == 1 and countC % 2 == 1:
        return 2
    return 1
    
if __name__ == '__main__':
    t = int(input())
    for i in range(0, t):
        a = input().strip()
        print(stringReduction(a))
