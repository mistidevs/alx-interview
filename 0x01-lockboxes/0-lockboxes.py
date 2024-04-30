#!/usr/bin/python3
"""
BFS Implementation
"""


def canUnlockAll(boxes):
    """
    Check if all the boxes can be unlocked.
    """
    visited = set([0])
    queue = boxes[0]

    while queue:
        box = queue.pop(0)

        if not box or box >= len(boxes) or box < 0:
            continue

        if box in visited:
            continue

        visited.append(box)
        if box < len(boxes) and boxes[box]:
            queue.extend(boxes[box])

    return len(visited) == len(boxes)
