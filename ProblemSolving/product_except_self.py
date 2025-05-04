# 238. Product of Array Except Self
# Approach: Prefix Sum and Suffix Sum. Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def productExceptSelf(nums: List[int]) -> List[int]:
        prefix_products,suffix_products = [],[]
        products = 1
        for i in nums:
            products *= i
            prefix_products.append(products)
        products = 1
        nums.reverse()
        for i in nums:
            products *= i
            suffix_products.append(products)
        suffix_products.reverse()
        
        nums[0] = suffix_products[1]
        nums[len(nums)-1] = prefix_products[len(nums)-2]
        for i in range(1,len(nums)-1):
            nums[i] = prefix_products[i-1] * suffix_products[i+1]
        return nums

print(productExceptSelf([1,2,3,4]))