# 28. Find the Index of the First Occurrence in a String
# Approach: linear search and slicing, Time Complexity: O(N)

def strStr(haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1

print(strStr("ramenramen","en"))