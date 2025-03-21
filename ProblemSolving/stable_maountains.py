# 3285. Find Indices of Stable Mountains
# Approach: Carry forward, Time Complexity: O(N), Space Complexity: O(1)

from typing import List 

def stableMountains(height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1,len(height)) if height[i-1]>threshold]

print(stableMountains([1,2,3,4,5],2))