# 268. Missing Number
# Approach: Gauss formula. Time Complexity: O(N), Space Complexity: O(1)

from typing import List

def missingNumber(nums: List[int]) -> int:
        return (max(nums) * (max(nums)+1) //2) - sum(nums) if (max(nums) * (max(nums)+1) //2) - sum(nums) not in nums else len(nums)

print(missingNumber([3,2,1]))