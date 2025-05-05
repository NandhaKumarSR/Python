# 41. First Missing Positive
# Approach: Marking the indexes. Time Complexity: O(N), Space Complexity: O(1)

from typing import List

def firstMissingPositive(nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] <= 0:
                nums[i] = len(nums) + 2

        for i in range(len(nums)):
            if abs(nums[i]) <= len(nums):
                nums[abs(nums[i])-1] = abs(nums[abs(nums[i])-1]) * -1
                
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1

        return len(nums)+1

print(firstMissingPositive([1,2,0]))