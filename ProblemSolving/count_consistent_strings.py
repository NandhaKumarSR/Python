# 1684. Count the Number of Consistent Strings

from typing import List

def countConsistentStrings(allowed: str, words: List[str]) -> int:
        count = 0
        allowed_strings = set(allowed)
        for i in words:
            if set(i).issubset(allowed_strings):
                count+=1
        return count

print(countConsistentStrings("ab",["ad","bd","aaab","baa","badab"]))