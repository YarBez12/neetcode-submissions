class Solution:
    def longestPalindrome(self, s: str) -> str:
        ans = [0,0]
        for i in range(len(s)):
            l, r = self.checkPalindrome(i, i, s)
            if r - l > ans[1]-ans[0]:
                ans = [l,r]
            l, r = self.checkPalindrome(i, i+1, s)
            if r - l > ans[1]-ans[0]:
                ans = [l,r]
        return s[ans[0]:ans[1]]
    
    def checkPalindrome(self, l, r, s):
        while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
        return l+1, r