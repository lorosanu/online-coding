from itertools import groupby

text = input().strip()
for chain,occ in groupby(text):
        print((len(list(occ)), int(chain)), end=' ')