n = int(input().strip())

x = [ int(z) for z in input().split()]
y = [ int(z) for z in input().split()]

x.sort()
y.sort()

if x == y:
    print(0)
elif n == 1 :
    print(-1)
else:
    sump = 0
    sumn = 0

    for i in range(n):
        if x[i] < y[i]:
            sumn += abs(x[i] - y[i])
        else:
            sump += x[i] - y[i]

    if sump != sumn:
        print(-1)
    else:
        print(sump)