# 894. Divisible and Non-divisible Sums Difference
# Approach: Arithmatic progression, Time Complexity: O(N)

def differenceOfSums(n: int, m: int) -> int:
        divisible_sum = m * (n//m * (n//m+1) //2)
        not_divisible_sum = n * (n+1)//2 - divisible_sum
        return not_divisible_sum - divisible_sum

print(differenceOfSums(5,1))