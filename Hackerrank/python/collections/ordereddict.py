from collections import OrderedDict

n = int(input())

products = OrderedDict()
for i in range(n):
    pq = input().strip()
    item = pq[0:pq.rfind(" ")]
    price = pq[pq.rfind(" ") + 1:]
    
    if item not in products:
        products[item] = int(price)
    else:
        products[item] += int(price)
        
for item, price in products.items():
    print(item, price)
