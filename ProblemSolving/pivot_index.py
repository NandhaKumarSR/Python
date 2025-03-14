# 724. Find Pivot Index
# Approach: Prefix Sum, Time Complexity: O(N)

from typing import List

def pivotIndex(nums: List[int]) -> int:
        prefix_sum = [0]
        sum = 0
        for i in nums:
            sum+=i 
            prefix_sum.append(sum)

        for i in range(1,len(prefix_sum)):
            lsum = prefix_sum[i-1]
            rsum = sum - prefix_sum[i]
            if lsum == rsum:
                return i-1

        return -1

print(pivotIndex([1,7,3,6,5,6]))