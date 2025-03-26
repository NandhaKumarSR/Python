# 1572. Matrix Diagonal Sum
# Approach: pattern identification, Time Complexity: O(N)  

from typing import List

def diagonalSum(mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            ans+= mat[i][i]
            if len(mat)-1-i != i:
                ans+= mat[i][len(mat)-1-i]
        return ans

print(diagonalSum([[1,2,3],[2,2,5],[2,8,9]]))