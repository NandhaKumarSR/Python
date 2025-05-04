# 3280. Convert Date to Binary

def convertDateToBinary(date: str) -> str:
        numbers = date.split('-')
        for i in range(len(numbers)):
            numbers[i] = str(bin(int(numbers[i])))[2:]
        return '-'.join(numbers)

print(convertDateToBinary("2080-02-29"))