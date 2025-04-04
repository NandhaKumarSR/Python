# 229. Majority Element II
# Approach: Boyer–Moore majority vote algorithm, Time Complexity: O(N), Space Complexity: O(1)

from typing import List

def majorityElement(nums: List[int]) -> List[int]:
        number1, number2 = None,None
        count1, count2 = 0,0
        for num in nums:
            if num == number1:
                count1 += 1
            elif num == number2:
                count2 += 1
            elif count1 == 0:
                number1 = num
                count1+=1
            elif count2 == 0:
                number2 = num
                count2+=1
            else:
                count1-=1
                count2-=1
        count1, count2 = 0,0
        for num in nums:
            if num == number1:
                count1+= 1
            elif num == number2:
                count2 += 1
        ans = []
        if count1 > len(nums)//3:
            ans.append(number1)
        if count2 > len(nums)//3:
            ans.append(number2)
        return ans

print(majorityElement([1,1,1,1,2,2,2,2,3,3]))