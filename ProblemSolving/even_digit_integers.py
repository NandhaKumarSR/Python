# 2180. Count Integers With Even Digit Sum
# Approach: Brute force

def countEven(num: int) -> int:
        count = 0
        for i in range(1,num+1):
            sum_digits = 0
            number = i
            while(number):
                sum_digits += number%10
                number//=10
            if sum_digits%2 == 0:
                count += 1
        return count

print(countEven(45))