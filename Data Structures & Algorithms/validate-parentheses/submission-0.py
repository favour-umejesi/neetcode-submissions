class Solution:
    def isValid(self, s: str) -> bool:
        matching = {
            "(": ")",
            "{": "}",
            "[": "]",
        }
        stack = []
        for c in s:
            if c in matching:
                stack.append(c)
            else:
                if not stack:
                    return False
                
                previous = stack.pop()
                if matching[previous] != c:
                    return False

        return not stack 
        