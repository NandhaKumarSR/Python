# 1688. Count of Matches in Tournament
# Approach: pattern eg: 7 -> 7/2 = 3 -> 4/2 = 2 -> 1 ===> 3+2+1 = 7-1

def numberOfMatches(n: int) -> int:
        return n-1

print(numberOfMatches(int(input('Enter number of teams: '))))