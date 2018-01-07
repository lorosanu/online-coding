import string 

n = int(input())
width = 4 * n - 3
letters = string.ascii_lowercase[:n]

patterns = []
for i in range(n-1, -1, -1):
    pattern1 = [ letter for letter in letters[i:] ]
    pattern2 = [ letter for letter in letters[i+1:] ]
    pattern1.reverse()
    
    pattern = pattern1 + pattern2        
    patterns.append("-".join(pattern).center(width, "-"))

for pattern in patterns:
    print(pattern)

for i in range(n-2, -1, -1):
    print(patterns[i])