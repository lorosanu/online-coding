n = int(input())
items = input().split()
wItems = list(items)

i = len(items) - 1
sortedA = False
while i > 0 and sortedA == False: 
    if items[i] < items[i-1]:
        items[i-1], items[i] = items[i], items[i-1]
        wItems[i] = wItems[i-1]
        print(" ".join(wItems))
    else:
        sortedA = True
    i-=1
    
print(" ".join(items))