#!/usr/bin/python3
"""
Module 0-lockboxes
Contains function canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened
    :param boxes: List of lists, where each list contains keys to other boxes
    :return: True if all boxes can be opened, else False
    """
    if not boxes or not isinstance(boxes, list):
        return False

    n = len(boxes)
    opened_boxes = [False] * n
    opened_boxes[0] = True
    keys = [0]

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened_boxes[key]:
                opened_boxes[key] = True
                keys.append(key)

    return all(opened_boxes)


# Ensuring the file ends with a new line
