#!/usr/bin/python3

def variableName(name):
    valid = re.compile('^[a-zA-Z\d_]*$')
    if re.match(valid, name) and not name[0].isdigit():
        return True
    return False

