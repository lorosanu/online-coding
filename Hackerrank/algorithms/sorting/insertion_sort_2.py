n = int(input())
items = input().split()

def placeItem(items, index):
    sortedA = False
    j = index
    while j > 0 and sortedA == False: 
        if int(items[j]) < int(items[j-1]):
            items[j-1], items[j] = items[j], items[j-1]        
        else:
            sortedA = True
        j-=1    
    return items
    
for x in range(1, len(items)):
    if int(items[x]) < int(items[x-1]):
        items = placeItem(items, x)
    print(" ".join(items))