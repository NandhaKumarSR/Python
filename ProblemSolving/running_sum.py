# 1480. Running Sum of 1d Array
# Approach: prefix sum TC: O(N)

from typing import List

def runningSum(nums: List[int]) -> List[int]:
        l1 = []
        a= 0
        for i in nums:
            a = a+i
            l1.append(a)
        return l1 

print(runningSum([1,2,3,4]))

