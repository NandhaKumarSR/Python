# 2022. Convert 1D Array Into 2D Array
# Approach: Brute Force, Time Complexity: O(M*N)

from typing import List

def construct2DArray(original: List[int], m: int, n: int) -> List[List[int]]:
        index = 0
        if m * n != len(original):
            return []
        matrix = []
        for i in range(m):
            inner_matrix = []
            for j in range(n):
                inner_matrix.append(original[index])
                index += 1
            matrix.append(inner_matrix)
        return matrix

print(construct2DArray([1,2,3,4],2,2))