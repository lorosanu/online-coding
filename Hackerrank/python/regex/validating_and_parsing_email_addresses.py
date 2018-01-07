import re

n = int(input().strip())
for i in range(n):
    name, email = (input().strip()).split()
    emailj = email[1:-1]
    
    res = bool(re.search(r"^([a-zA-Z][a-zA-Z0-9-_\.]*)@([a-zA-Z]+)\.([a-zA-Z]{1,3})$", emailj))
    if res:
        print(name, email)