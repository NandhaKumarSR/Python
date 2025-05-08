# 136. Single Number
# Approach: Bit manipulation. Time Complexity: O(N), Space Complexity: O(1)

from typing import List

def singleNumber(nums: List[int]) -> int:
        first = nums[0]
        for i in nums[1:]:
            first ^= i
        return first  

print(singleNumber([2,2,1]))      