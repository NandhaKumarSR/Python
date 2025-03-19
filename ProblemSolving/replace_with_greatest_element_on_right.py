# 1299. Replace Elements with Greatest Element on Right Side
# Approach: Carry forward technique, Time Complexity: O(N)

from typing import List

def replaceElements(arr: List[int]) -> List[int]:
        max_num = -1
        for i in range(len(arr)-1,-1,-1):
            temp = arr[i]
            arr[i] = max_num
            if(temp > max_num):
                max_num = temp
        return arr

print(replaceElements([6,2,7,4,5]))