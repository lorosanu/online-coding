vowels = ['A', 'E', 'I', 'O', 'U']

text = input()
N = len(text)

kevin_score = 0
stuart_score = 0
for i in range(len(text)):
    if text[i] in vowels:
        kevin_score += (N - i)
    else:
        stuart_score += (N - i)

if kevin_score > stuart_score:
    print("Kevin",kevin_score)
elif stuart_score > kevin_score:
    print("Stuart",stuart_score)
else:
    print("Draw")