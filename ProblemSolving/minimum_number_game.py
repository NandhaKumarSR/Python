# 2974. Minimum Number Game
# Approach: Bruteforce: Sort and Replace nlogn time complexity

from typing import List

def numberGame(nums: List[int]) -> List[int]:
        nums.sort()
        i=0
        while(i+1 < len(nums)):
            temp = nums[i+1]
            nums[i+1] = nums[i]
            nums[i] = temp
            i+=2 

        return nums

print(numberGame([5,4,7,8]))