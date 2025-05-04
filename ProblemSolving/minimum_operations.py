# 3396. Minimum Number of Operations to Make Elements in Array Distinct
# Approach: using set data structure. Time Complexity: O(N^2)

from typing import List

def minimumOperations(nums: List[int]) -> int:
        
        swaps = 0
        for i in range(0,len(nums),3):
            if len(set(nums[i:len(nums)])) != len(nums[i:len(nums)]):
                swaps +=1

        return swaps

print(minimumOperations([1,2,3,4,2,3,3,5,7]))