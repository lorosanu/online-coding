#!/usr/bin/python3

def chessBoardCellColor(cell1, cell2):
    dx = abs(ord(cell1[0]) - ord(cell2[0]))
    dy = abs(int(cell1[1]) - int(cell2[1]))
    if (dx + dy) % 2 == 1:
        return False
    return True

