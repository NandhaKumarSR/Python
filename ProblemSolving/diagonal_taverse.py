# 498. Diagonal Traverse
# Approach: Pattern Identification, Time complexity: O(N∗M∗Log(Min(N,M)))

from typing import List

def findDiagonalOrder(mat: List[List[int]]) -> List[int]:
        if not mat or not mat[0]: 
            return []

        rows, cols = len(mat), len(mat[0])
        result = []
        diagonals = {}

        for i in range(rows):
            for j in range(cols):
                if i + j not in diagonals:
                    diagonals[i + j] = []
                diagonals[i + j].append(mat[i][j])


        for key in sorted(diagonals.keys()):
            if key % 2 == 0:
                result.extend(diagonals[key][::-1]) 
            else:
                result.extend(diagonals[key])

        return result