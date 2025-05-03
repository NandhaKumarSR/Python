# 2016. Maximum Difference Between Increasing Elements
# Approach: Carry forward technique. Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def maximumDifference(nums: List[int]) -> int:
        left_min,right_max = [],[]
        curr_min,curr_max = nums[0], nums[-1]
        max_difference = 0
        for i in nums:
            curr_min = min(curr_min, i)
            left_min.append(curr_min)
        for i in nums[::-1]:
            curr_max = max(curr_max,i)
            right_max.append(i)
        right_max.reverse()

        for i in range(len(nums)):
            max_difference = max(max_difference, right_max[i] - left_min[i])
        
        return max_difference if max_difference > 0 else -1

print(maximumDifference([7,1,5,4]))