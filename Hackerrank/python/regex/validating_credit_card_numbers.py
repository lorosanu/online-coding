import re

n = int(input().strip())
for i in range(n):
    id = input().strip()
    if bool(re.search(r"^([0-9]{4})([-]?[0-9]{4}){3}$", id) and re.search(r"^[456]", id)):
        id = re.sub(r"-", r"", id)
        if not bool(re.search(r"([0-9])\1{3,}", id)):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")