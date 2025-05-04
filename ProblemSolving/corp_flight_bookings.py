# 1109. Corporate Flight Bookings

from typing import List

def corpFlightBookings(bookings: List[List[int]], n: int) -> List[int]:
        reserved = [0]*n
        for b in bookings:
            reserved[b[0]-1] += b[2]
            if b[1] != n:
                reserved[b[1]] -= b[2]
        for i in range(1,n):
            reserved[i] += reserved[i-1]
        return reserved

print(corpFlightBookings([[1,2,10],[2,3,20],[2,5,25]],5))