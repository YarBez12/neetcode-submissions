class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            if not (ord ("A") <= ord(s[l]) <= ord("Z") or ord ("a") <= ord(s[l]) <= ord("z") or ord ("0") <= ord(s[l]) <= ord("9")):
                l += 1
            elif not (ord ("A") <= ord(s[r]) <= ord("Z") or ord ("a") <= ord(s[r]) <= ord("z") or ord ("0") <= ord(s[r]) <= ord("9")):
                r -= 1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l +=1
                r -=1
        return True
        