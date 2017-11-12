#!/usr/bin/python3

def firstDigit(inputString):
    return re.search('\d', inputString).group(0)

