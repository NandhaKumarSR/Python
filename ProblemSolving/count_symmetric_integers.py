# 2843. Count Symmetric Integers

def countSymmetricIntegers(low: int, high: int) -> int:
        count = 0
        while(low <= high):
            string_value = str(low)
            digits = len(string_value)
            if  digits % 2 != 0:
                low = 10**(digits)
            else:
                if sum( [int(string_value[i]) for i in range(digits//2)]) == sum([int(string_value[i]) for i in range(digits//2,digits)]):
                    count +=1
                low+=1
        return count 

print(countSymmetricIntegers(1,100))