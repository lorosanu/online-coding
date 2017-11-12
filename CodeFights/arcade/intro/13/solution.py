#!/usr/bin/python3

def rindex(mylist, myvalue):
    return len(mylist) - mylist[::-1].index(myvalue) - 1

def reverseParentheses(s):
    sv = [c for c in s]
    opened, closed = [], []
    for index, c in enumerate(sv):
        if c == '(':
            opened.append(index + 1)
            closed.append(-1)
        elif c == ')':
            lindex = rindex(closed, -1)
            closed[lindex] = index
    for i in range(len(opened) - 1, -1, -1):
        start = opened[i]
        end = closed[i]
        sv[start:end] = list(reversed(sv[start:end]))
    s = ''.join(sv)
    return re.sub("[\(\)]", '', s)

