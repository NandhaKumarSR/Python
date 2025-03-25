# 1394. Find Lucky Integer in an Array
# Approach: Hashmap, Time Complexity: O(N), Space Complexity: O(N)

from typing import List

def findLucky(arr: List[int]) -> int:
        frequency_map = {}
        for i in arr:
            if i in frequency_map.keys():
                frequency_map[i]+=1
            else:
                frequency_map[i]=1
        lucky_integer = -1
        for key,value in frequency_map.items():
            if key == value:
                lucky_integer = max(lucky_integer, key)
        return lucky_integer

print(findLucky([1,22,22,1,2,3,2]))