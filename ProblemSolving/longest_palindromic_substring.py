# 5. Longest Palindromic Substring
# Approach: Two pointers. Time Complexity: O(N^2), Space Complexity: O(1)

def longestPalindrome(s: str) -> str:
        start_index = 0
        end_index = 0
        max_length = 0
        for i in range(len(s)):
            start,end, length = i,i,0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                length = end - start + 1
                start -= 1
                end += 1
            if length > max_length:
                max_length = length
                start_index = start+1
                end_index = end
        for i in range(len(s)):
            start,end, length = i,i+1,0
            while start >= 0 and end < len(s) and s[start] == s[end]:
                length = end - start + 1
                start -= 1
                end += 1
            if length > max_length:
                max_length = length
                start_index = start+1
                end_index = end
        return s[start_index: end_index]

print(longestPalindrome("nandha kumar"))