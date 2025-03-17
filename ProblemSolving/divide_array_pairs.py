# 206. Divide Array Into Equal Pairs
# Approach: Hash Map, Time Complexity: O(N)

from typing import List

def divideArray(nums: List[int]) -> bool:
        freq = {}

        for i in nums:
            if i not in freq.keys():
                freq[i]  = 1
            else:
                freq[i] += 1

        for i in freq.values():
            if i % 2 != 0:
                return False
        
        return True

print(divideArray([3,3,2,2,1,1]))

