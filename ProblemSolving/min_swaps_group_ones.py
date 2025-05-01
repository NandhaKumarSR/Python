# 2134. Minimum Swaps to Group All 1's Together II
from typing import List

def minSwaps(nums: List[int]) -> int:
        count_sum = sum(nums)
        if count_sum in [len(nums),0]:
            return 0
        sum_range = sum(nums[0:count_sum])
        
        min_swaps = count_sum - sum_range

        for i in range(count_sum, len(nums)*2):
            sum_range = sum_range - nums[i%len(nums) - count_sum] + nums[i%len(nums)]
            min_swaps = min(min_swaps, count_sum - sum_range)
        
        return min_swaps
print(minSwaps([0,1,0,1,1,0,0]))