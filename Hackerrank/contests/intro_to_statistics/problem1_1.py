from math import *

def compute_mean(n, numbers):
    sum = 0
    for x in numbers:
        sum += x
    mean = sum/n
    return mean

def compute_median(n, numbers):
    median = 0
    index = n//2

    sorted_numbers = sorted(numbers)

    if ( n % 2 == 1):
        median = sorted_numbers[index]
    else:
        median = (sorted_numbers[index-1] + sorted_numbers[index] ) / 2

    return median

def compute_mode(n, numbers):
    sorted_numbers = sorted(numbers)
    most_frequent = sorted_numbers[n - 1]
    frequency = 0
    
    for x in numbers:
        nc = numbers.count(x)
        if nc > frequency :
            frequency = nc
            most_frequent = x
        elif nc == frequency and x <= most_frequent:
            most_frequent = x

    return most_frequent

def compute_sd(n, numbers, mean):
    sd = 0
    for x in numbers:
        sd += (x - mean)**2
    sd = sqrt(sd / n)
    return sd


n = int(input())
numbers = [int(x) for x in input().split()]

mean = compute_mean(n, numbers)
median = compute_median(n, numbers)
most_frequent = compute_mode(n, numbers)
sd = compute_sd(n, numbers, mean)

mean = "{:0.1f}".format(mean)
median = "{:0.1f}".format(median)
sd = "{:0.1f}".format(sd)

print(mean)
print(median)
print(most_frequent)
print(sd)
