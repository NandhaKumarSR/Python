# 2529. Maximum Count of Positive Integer and Negative Integer
# Approach: carry forward technique, Time Complexity: O(N)

from typing import List

def maximumCount(nums: List[int]) -> int:
        positive, negative = 0, 0
        for i in nums:
            if i > 0:
                positive += 1
            elif i < 0:
                negative += 1
        return max(positive,negative) 

print(maximumCount([1,-1,-5,7]))

