# 1207. Unique Number of Occurrences
# Approach: HashMap, Time Complexity: O(N)


from typing import List

def uniqueOccurrences(arr: List[int]) -> bool:
        freq = {}
        for i in arr:
            if i in freq:
                freq[i] += 1
            else:
                freq[i] = 1
        return True if len(freq.keys()) == len(set(freq.values())) else False 

print(uniqueOccurrences([1,2,2,3,3,3,4,4,4,4]))