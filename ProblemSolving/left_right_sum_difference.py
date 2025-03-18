# 2574. Left and Right Sum Differences
# Approach: prefix sum, Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def leftRightDifference(nums: List[int]) -> List[int]:
        pf = [nums[0]]
        for i in range(1,len(nums)):
            pf.append(pf[i-1]+nums[i])

        output_array = []        
        for i in range(len(nums)):
            if i != 0:
                output_array.append(abs(pf[i-1] - (pf[len(nums)-1] - pf[i])))
            else:
                output_array.append(abs((pf[len(nums)-1] - pf[i])))

        return output_array

print(leftRightDifference([1,2,3,4,5,10]))