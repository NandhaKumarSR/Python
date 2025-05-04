# 2176. Count Equal and Divisible Pairs in an Array

from typing import List

def countPairs(nums: List[int], k: int) -> int:
        count = 0
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if i * j  % k == 0 and nums[i] == nums[j]:
                    count += 1
        return count

print(countPairs([3,1,2,2,2,1,3],2))