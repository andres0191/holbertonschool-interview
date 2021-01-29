#!/usr/bin/python3
"""
You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n - 1
and each box may contain keys to the other boxes.
Write a method that determines if all the boxes
can be opened.
* Prototype: def canUnlockAll(boxes)
* boxes is a list of lists
* A key with the same number as a box opens that box
- You can assume all keys will be positive integers
* The first box boxes[0] is unlocked
* Return True if all boxes can be opened, else return False
"""

def canUnlockAll(boxes):
    """ validate if all the boxes can be opened
    """
    arr = [0]
    if (len(boxes) == 0):
        return True
    for i in arr:
        for i_box in boxes[i]:
            if i_box not in arr:
                if i_box < len(boxes):
                    arr.append(i_box)
    if len(arr) == len(boxes):
        return True
    return False