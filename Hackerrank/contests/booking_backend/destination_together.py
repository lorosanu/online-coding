import math

n, m, c = [int(x) for x in input().split()]
diff = m + n - c -1

print(math.factorial(diff))
