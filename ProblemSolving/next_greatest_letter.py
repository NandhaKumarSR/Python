# 744. Find Smallest Letter Greater Than Target
# Approach: ASCII order, Time Complexity: O(N)

from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
        for i in letters:
            if ord(i) > ord(target):
                return i
        return letters[0]

print(nextGreatestLetter(["c","f","j"],"a"))