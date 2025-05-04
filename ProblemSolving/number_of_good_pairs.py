# 3162. Find the Number of Good Pairs I

from typing import List

def numberOfPairs(nums1: List[int], nums2: List[int], k: int) -> int:
        num2 = [i * k for i in nums2]
        num2_freq = {}
        count = 0

        for i in num2:
            if i in num2_freq.keys():
                num2_freq[i] += 1
            else:
                num2_freq[i] = 1

        for i in nums1:
            for j in range(1,int(i**0.5)+1):
                if i % j == 0:
                    if j != i//j:
                        if i // j in num2_freq.keys():
                            count += num2_freq[i//j]
                        if j in num2_freq.keys():
                            count += num2_freq[j]
                    else:
                        if j in num2_freq.keys():
                            count += num2_freq[j]
        return count

print(numberOfPairs([1,3,4],[1,3,4],1))