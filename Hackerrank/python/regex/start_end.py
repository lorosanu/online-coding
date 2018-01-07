import re

text = input().strip()
sub = input().strip()

if re.search(sub, text):
    for i in range(len(text)):        
        m = re.match(sub, text[i:])
        if m : 
            print((i + m.start(), i + m.end() -1))
else:
    print('(-1, -1)')