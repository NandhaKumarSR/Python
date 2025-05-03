# 121. Best Time to Buy and Sell Stock
# Approach: Carry forward technique. Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def maxProfit(prices: List[int]) -> int:
        left_min,right_max = [],[]
        curr_min,curr_max = prices[0], prices[-1]
        max_profit = 0
        for i in prices:
            curr_min = min(curr_min, i)
            left_min.append(curr_min)
        for i in prices[::-1]:
            curr_max = max(curr_max,i)
            right_max.append(i)
        right_max.reverse()

        for i in range(len(prices)):
            max_profit = max(max_profit, right_max[i] - left_min[i])
        
        return max_profit

print(maxProfit([7,1,5,3,6,4]))