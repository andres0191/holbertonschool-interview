#!/usr/bin/python3
"""
Module for 0-rain.py
0x10. Rain
Specializations - Interview Preparation ― Algorithms
"""
# walls = [0,1,0,2,1,0,1,3,2,1,2,1]


def rain(walls):
    """With notes to myself thanks to YT """
    lenght = len(walls)
    water = 0
    #  We will build two arrays with the highest possible level of water
    #  one from left to right and one from right to left
    leftMax, rightMax = [0] * lenght, [0] * lenght

    if not walls or lenght < 3:
        return 0

    leftMax[0] = walls[0]
    rightMax[lenght - 1] = walls[lenght - 1]

    for i in range(1, lenght):
        leftMax[i] = max(leftMax[i - 1], walls[i])
    for i in range(lenght - 2, -1, -1):
        rightMax[i] = max(rightMax[i + 1], walls[i])
    for i in range(lenght):
        water = water + min(leftMax[i], rightMax[i]) - walls[i]

    return water
