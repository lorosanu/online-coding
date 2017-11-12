#!/usr/bin/python3

def isIPv4Address(s):
    fields = s.split('.')
    if len(fields) != 4:
        return False

    for x in fields:
        if not x or not x.isdigit():
            return False
        ix = int(x)
        if ix < 0 or ix > 255:
            return False
    return True

