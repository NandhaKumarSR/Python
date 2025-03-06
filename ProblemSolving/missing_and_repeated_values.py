# 2965. Find Missing and Repeated Values
# Approach: Using set and carry forward technique - time complextity O(N)

from typing import List

def findMissingAndRepeatedValues(grid: List[List[int]]) -> List[int]:
        n = len(grid)
        N = n * n
        s = set([])
        sum_list = 0
        for i in grid:
            s.update(set(i))
            sum_list+= sum(i)
        repeated_num = sum_list - sum(s)
        missing_num = N * (N+1) // 2 - sum(s)
        return [repeated_num, missing_num]

print(findMissingAndRepeatedValues([[1,3],[2,2]]))