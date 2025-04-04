# 3467. Transform Array by Parity

from typing import List

def transformArray(nums: List[int]) -> List[int]:
        count = 0
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
                count += 1
        for i in range(len(nums)-count):
            nums[i] = 0
        for i in range(len(nums)-count,len(nums)):
            nums[i] = 1
        return nums

print(transformArray([1,2,3,4,5]))