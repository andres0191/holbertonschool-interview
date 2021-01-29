#!/usr/bin/python3
"""  """

def canUnlockAll(boxes):
    i = 0
    if(type(boxes) is not list):
        return False
    if(len(boxes) == 0):
        return False
    for i in (boxes):
        if(len(boxes[i]) > 0):
            for j in (boxes[i]):
                if(len(boxes[j]) == 0)
                    return False
    return True