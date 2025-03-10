# 1512. Number of Good Pairs
# Approach: Subarrays

from typing import List

def numIdenticalPairs(nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if i+1<len(nums):
                for j in range(i+1,len(nums)):
                    if nums[i] == nums[j]:
                        count+=1
        return count

print(numIdenticalPairs([1,2,3,1,2]))