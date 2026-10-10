class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = ""
        for i in range(len(s)):
            r = self.checkPalindrome(i, i, s)
            if len(r) > len(ans):
                ans = r
            r = self.checkPalindrome(i, i+1, s)
            if len(r) > len(ans):
                ans = r
        return ans
    
    def checkPalindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        return s[l+1:r]