s = input()
k = int(input())

pos = 0
nparts = len(s) // k

for i in range(nparts):
    t = s[pos:pos + k]
    sol = ""
    for letter in t :
        if letter not in sol:
            sol += letter
    print(sol)
    pos += k