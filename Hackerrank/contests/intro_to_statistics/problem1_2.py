from math import *

def computeSD(numbers):
    n = len(numbers)

    # compute mean
    sum = 0
    for x in numbers:
        sum += x
    mean = sum/n

    # compute SD
    SD = 0
    for x in numbers:
        SD += (x - mean)*(x-mean)
    SD = sqrt(SD/n)

    SD = round(SD, 4)        
    return SD

def checkNumber(numbers, oldSD):
    M = 0.00
    maxValue = 0
    found = False
    while not found:
        newVector = list(numbers)
        newVector.append(M)        
        newSD = computeSD(newVector)        

        if ( abs(newSD - oldSD) <= 0.001 ):   
            maxValue = M         
            print()
            print("newValue={}, newSD={}", M, newSD)

        if ( abs(newSD - oldSD) >= 10 ):   
            found = True

        M = M + 0.01
        M = round(M, 2)

    maxValue = round(maxValue, 2)
    return maxValue

numbers = [1, 2, 3]
oldSD = computeSD(numbers)

print("Reference numbers=", numbers)
print("Reference SD=", oldSD)

M = checkNumber(numbers, oldSD)
print(M)

numbers = [1, 2, 3, M]
newSD = computeSD(numbers)

print("Old SD = {}, new SD = {}".format(oldSD, newSD))
      
