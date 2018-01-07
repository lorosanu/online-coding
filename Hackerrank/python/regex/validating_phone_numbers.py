import re

n = int(input().strip())
for i in range(n):
    text = input()
    res = bool(re.search(r"^[789][0-9]{9}$", text))
    if res:
        print("YES")
    else:
        print("NO")
    