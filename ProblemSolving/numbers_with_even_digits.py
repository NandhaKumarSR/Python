# 1295. Find Numbers with Even Number of Digits

from typing import List

def findNumbers(nums: List[int]) -> int:
        count = 0
        for i in nums:
            if len(str(i)) %2 == 0:
                count += 1
        return count

print(findNumbers([12,345,2,6,7896]))