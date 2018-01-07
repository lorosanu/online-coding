from collections import Counter
from operator import itemgetter

d = Counter(input())

values = sorted(set(d.values()), reverse=True)
keys = sorted(set(d.keys()))

count = 0
for occ in values:
    for item in keys:
        if d[item] == occ and count < 3:
            print(item, occ)
            count += 1
    
