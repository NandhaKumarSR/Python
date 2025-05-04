# 42. Trapping Rain Water
# Approach: Carry Forward Technique. Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def trap(height: List[int]) -> int:
        r_max = height[len(height) - 1]
        l_max = height[0]
        left = []
        right = []
        for i in range(len(height)):
            r_max = max(r_max, height[len(height) - 1 -i])
            l_max = max(l_max, height[i])
            left.append(l_max)
            right.append(r_max)
        
        right.reverse()
        water_trapped = 0

        for i in range(len(height)):
            water_trapped += min(left[i],right[i]) - height[i]

        return water_trapped

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
