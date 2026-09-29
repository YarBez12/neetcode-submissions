class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ans = []
        self.check(s, 0, [], "", ans)
        return ans


    def check(self, s, ind, currPart, currStr, ans):
        if ind == len(s):
            ans.append(currPart.copy())
        for i in range(ind, len(s)):
            currStr += s[i]
            if self.isPalindrome(currStr):
                currPart.append(currStr)
                self.check(s, i+1, currPart, "", ans)
                currPart.pop()


    def isPalindrome(self, s):
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -=1 
        return True
        