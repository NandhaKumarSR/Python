# 3375. Minimum Operations to Make Array Values Equal to K

from typing import List

def minOperations(nums: List[int], k: int) -> int:
        l = []
        for i in nums:
            if i<k:
                return -1
            elif i>k:
                l.append(i)
        return len(set(l))

print(minOperations([5,2,5,4,5],2))