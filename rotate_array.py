# 189. Rotate Array
# Approach: Identifying the pattern and reversing the array with time complexity O(N)

from typing import List

def rotate(nums: List[int], k: int) -> None:
        K = k % len(nums)
        nums.reverse()
        i = 0
        j = K-1
        while(i < j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
        i = K
        j = len(nums) - 1
        while(i < j):
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp
            i+=1
            j-=1
n = [10,9,8,7]
rotate(n,2)
print(n)