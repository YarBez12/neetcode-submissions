class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[0] = True
        for i in range(len(s)):
            letter = s[i]
            ret = False
            for word in wordDict:
                l = len(word)
                if word[-1] == letter and i-l+1 >= 0 and s[i-l+1:i+1] == word and dp[i-l+1]:
                    ret = True
                    break
            dp[i+1] = ret
        return dp[-1]
        