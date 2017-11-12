#!/usr/bin/python3

def boxBlur(image):
    n = len(image) - 2
    m = len(image[0]) - 2
    box = [[0 for i in range(m)] for j in range(n)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            box[i-1][j-1] = math.floor(
                (sum(image[i-1][j-1:j+2]) +
                 sum(image[i][j-1:j+2]) +
                 sum(image[i+1][j-1:j+2])
                ) / 9.0
            )
    return box

