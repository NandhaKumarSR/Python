# 1662. Check If Two String Arrays are Equivalent
# Approch: using join method

from typing import List

def arrayStringsAreEqual(word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)

arrayStringsAreEqual(["ab","c"],["a","bc"])