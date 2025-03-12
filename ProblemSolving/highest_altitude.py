# 1732. Find the Highest Altitude
# Approach: Prefix sum, Time Complexity O(N)


from typing import List

def largestAltitude(gain: List[int]) -> int:
        s = 0
        ps =[0]
        for i in gain:
            s+= i
            ps.append(s)
        return max(ps)

print(largestAltitude([-1,-4,-5,-8,9,24,66]))