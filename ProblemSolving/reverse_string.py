# 344. Reverse String
# Approach: swapping

from typing import List

def reverseString(s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        for i in range(len(s)//2):
            temp = s[i]
            s[i] = s[len(s) - 1 - i]
            s[len(s) - 1 - i] = temp

s = ["H","a","n","n","a","h"]
reverseString(s)
print(s)
