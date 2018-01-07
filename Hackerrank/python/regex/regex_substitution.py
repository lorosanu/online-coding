import re

n = int(input().strip())

for i in range(n):
    text = input()
    rtext = text    
    if re.search(r" && ", text) or re.search(r" \|\| ", text):
        rtext = text
        while re.search(r" && ", rtext) or re.search(r" \|\| ", rtext):
            rtext = re.sub(r" && ", " and ", rtext)
            rtext = re.sub(r" \|\| ", " or ", rtext)
        print(rtext)
    else:
        print(text)