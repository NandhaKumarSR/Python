# 20. Valid Parentheses
# Approach: Stack, Time Complexity: O(N)

def isValid(s: str) -> bool:
    parenthesis = [0]
    parenthesis_map = {
        "}":"{",
        ")" :"(",
        "]" : "["
    }
    for i in range(len(s)):
        if s[i] in parenthesis_map.values():
            parenthesis.append(s[i])
        elif parenthesis[-1] != parenthesis_map[s[i]]:
            return False
        else:
            parenthesis.pop()
    return True if len(parenthesis) == 1 else False

print(isValid("{{{}{}{}{}{}{}{}{[][][][](((((((((())))))))))}}}"))