import sys

def solution(A):
    n = len(A)
    psum = [0] * (n + 1)
    
    min_avg = sys.maxint
    min_index = 0

    for i in range(1, n + 1):
        psum[i] = psum[i - 1] + A[i - 1]               

        if i >= 2:
            prev_2 = (psum[i] - psum[i - 2]) / 2.0          # check prev 2 slices
            if prev_2 <  min_avg:
                min_avg = prev_2
                min_index = i-2

        if i >= 3:                                          # check prev 3 slices if we have calculated 3 prefix sums
            prev_3 = (psum[i] - psum[i - 3]) / 3.0

            if prev_3 < min_avg:
                min_avg = prev_3
                min_index = i-3

    return min_index
