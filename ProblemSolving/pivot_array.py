# 2161. Partition Array According to Given Pivot

from typing import List

def pivotArray(nums: List[int], pivot: int) -> List[int]:
        left = []
        middle = []
        right = []
        for num in nums:
            if num < pivot:
                left.append(num)
            elif num > pivot:
                right.append(num)
            else:
                middle.append(num)
        return left  + middle + right

print(pivotArray([9,12,5,10,14,3,10],10))