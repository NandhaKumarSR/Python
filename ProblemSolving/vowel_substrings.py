# 2062. Count Vowel Substrings of a String
# Approach: Subarrays, Time Complexity: O(N^2)

def countVowelSubstrings(word: str) -> int:
        count = 0
        for i in range(len(word)):
            for j in range(i+5,len(word)+1):
                if {'a','e','i','o','u'} == set(word[i:j]):
                    count +=1
        return count

print(countVowelSubstrings("asdfghjkaeiasdfgouaeiou"))