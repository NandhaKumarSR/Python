# 169. Majority Element
# Approach: Boyer–Moore majority vote algorithm, Time Complexity: O(N), Space Complexity: O(1)

from typing import List

def majorityElement(nums: List[int]) -> int:
        number = None
        count = 0
        for num in nums:
            if num == number:
                count += 1
            elif count == 0:
                number = num
                count += 1
            else:
                count-=1
        count = 0
        return number  

print(majorityElement([1,1,1,2,2]))