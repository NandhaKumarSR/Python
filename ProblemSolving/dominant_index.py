# 747. Largest Number At Least Twice of Others

from typing import List

def dominantIndex(nums: List[int]) -> int:
        max_element = max(nums)
        index = nums.index(max_element)
        second_max = -1
        for num in nums:
            if num > second_max and num < max_element:
                second_max = num
        return index if max_element >= second_max * 2 else -1

print(dominantIndex([1,2,3,6]))
