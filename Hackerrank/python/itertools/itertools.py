from itertools import product, permutations, combinations, combinations_with_replacement, groupby

a = [1, 2]
b = [3, 4]
print("\nProduct between (1,2) and (3,4)")
for x in list(product(a,b)):
    print(x, end=" ")


text = "123"
w = 2

print("\n\nPermutations of maximum 2-items from [1,2,3] ")
for i in range(1,w+1):
    for chain in permutations(text, i):
        print("".join(chain))

text = sorted("HACK")
w = 2
print("\nPermutations of maximum 2-items from [A,C,H,K] ")
for i in range(1,w+1):
    for chain in permutations(text, i):
        print("".join(chain))
        
print("\nCombinations of maximum 2-items from [A,C,H,K] ")
for i in range(1,w+1):
    for chain in combinations(text, i):
        print("".join(chain))

print("\nCombinations with replacement of maximum 2-items from [A,C,H,K] ")
for i in range(1,w+1):
    for chain in combinations_with_replacement(text, i):
        print("".join(chain))

text = "1222311"
print("\nGroupby on 1222311")
for chain,occ in groupby(text):
        print((len(list(occ)), int(chain)), end=' ')


    
