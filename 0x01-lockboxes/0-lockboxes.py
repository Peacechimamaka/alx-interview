#!/usr/bin/python3
"""
This module contains the function `canUnlockAll`.

Each box is numbered sequentially from 0 to n - 1 and
Box 0 is initially unlocked.

Example Usage:
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
"""
    def canUnlockAll(boxes):
        """
        Determines if all boxes can be opened.

        Args:
            boxes (list of list of int):

        Returns:
            bool: True if all boxes can be opened, False otherwise.
        """
        n = len(boxes)
        opened = set()
        stack = [0]

        while stack:
            box = stack.pop()
            if box not in opened:
                opened.add(box)
                for key in boxes[box]:
                    if key < n:
                        stack.append(key)

        return len(opened) == n

# Test cases
    if __name__ == "__main__":
        boxes = [[1], [2], [3], [4], []]
        print(canUnlockAll(boxes))  # True

        boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
        print(canUnlockAll(boxes))  # True

        boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
        print(canUnlockAll(boxes))  # False
