# 2091. Removing Minimum and Maximum From Array
# Approach: Brute force

from typing import List

def minimumDeletions(nums: List[int]) -> int:
        min_element = min(nums)
        max_element = max(nums)
        min_element_position, max_element_position,position  = 0,0,0
        for i in nums:
            if i == min_element:
                min_element_position = position
            elif i == max_element:
                max_element_position = position
            position +=1
        nums_length = len(nums)
        deleting_from_start = max(max_element_position,min_element_position) + 1
        deleting_from_end = len(nums) - min(max_element_position,min_element_position)
        min_delete = min(min_element_position+1, len(nums) - min_element_position)
        max_delete = min(max_element_position+1, len(nums) - max_element_position)
        deleting_separately = min_delete + max_delete
        return  min([deleting_from_start,deleting_from_end,deleting_separately])

print(minimumDeletions([3,4,6,10,24,18,1]))