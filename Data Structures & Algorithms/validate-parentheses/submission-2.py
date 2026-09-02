class Solution:
    def isValid(self, s: str) -> bool:
        m = {
            "{": "}",
            "(": ")",
            "[": "]"
        }
        stack = []
        for c in s:
            if c in "({[":
                stack.append(c)
            elif len(stack) == 0 or c != m[stack[-1]]:
                return False
            else:
                stack.pop()
        
        return len(stack) == 0

        