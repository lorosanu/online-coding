vowels = "aeiouAEIOU"

n = int(input().strip())

for i in range(n):
    text = input().strip()
    items = []
    itemsc = []
    for char in text:
        if char in vowels:
            items.append(char)
        else:
            items.append(".")
            itemsc.append(char)

    itemsc.reverse()
    k = 0
    for i in range(len(items)):
        if items[i] == ".":
            items[i] = itemsc[k]
            k += 1

    print("".join(items))
