# 507. Perfect Number
# Approach: Sqrt(N) Time complexity

def checkPerfectNumber(num: int) -> bool:
        sum = 0
        for i in range(1,int(num**0.5)+1):
            if num%i == 0:
                if i == num/i:
                    sum+=i
                else:
                    sum+=i+num/i
        return True if sum-num == num else False

print(checkPerfectNumber(int(input("Enter a Number: "))))