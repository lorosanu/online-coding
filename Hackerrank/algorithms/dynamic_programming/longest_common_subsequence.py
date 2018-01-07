def LCS(a, b, n, m):
    d = [[0 for y in range(m + 1)] for x in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if a[i - 1] == b[j - 1]:
                d[i][j] = d[i - 1][j - 1] + 1
            else:                
                d[i][j] = max(d[i - 1][j], d[i][j - 1])
                
    return d

def backtrack(d, a, b, i, j):
    if i == 0 or j == 0:
        return ""
    elif a[i - 1] == b[j - 1]:
        return str(a[i - 1]) + " " + backtrack(d, a, b, i - 1, j - 1)
    elif d[i - 1][j] > d[i][j - 1]:
        return backtrack(d, a, b, i - 1, j)
    else:
        return backtrack(d, a, b, i, j - 1)
    

n, m = [int(x) for x in input().split()]
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
        
d = LCS(a, b, n, m)
sol = backtrack(d, a, b, n, m)
print(" ".join(list(reversed(sol.split()))))