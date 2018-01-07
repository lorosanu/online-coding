
def splitArray(items, left, right, sumT, score):  
    global maxScore    

    if score > maxScore:
        maxScore = score

    if right > len(items) or right < left or sumT % 2 == 1 or right == left or right == left + 1 :
        return 0
    else:
        sumC = 0
        i = left
        while i < right and sumC <= sumT // 2:
            sumC += items[i]
            if ( sumC == sumT // 2 ):
                score = score + 1
                return splitArray(items, left, i+1, sumC, score) + splitArray(items, i+1, right, sumC, score)
            i += 1
            
    return 0
    

T = int(input().strip())
for k in range(T):
    N = int(input().strip())
    items = [int(x) for x in input().strip().split() ]
    
    sum = 0
    for x in items:
        sum += x
    
    if sum % 2 == 1:
        print(0)
    elif sum == 0 and items.count(0) == len(items):
        print(len(items)-1)
    else:
        maxScore = 0
        splitArray(items, 0, len(items), sum, 0)
        print(maxScore)
    
    
