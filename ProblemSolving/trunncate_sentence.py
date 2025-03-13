# 1816. Truncate Sentence
# Approach: carry forward technique, Time Complexity: O(N)

def truncateSentence(s: str, k: int) -> str:
        space = 0
        position = 0
        for i in s:
            if i == " ":
                space += 1
            if space == k:
                break
            position+=1
        
        return s if space < k else s[0:position]

print(truncateSentence("Hello World How are you",2))