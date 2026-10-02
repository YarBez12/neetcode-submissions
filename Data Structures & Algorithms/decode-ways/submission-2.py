class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1
        for i in range(1, len(s)):
            x1, x2 = int(s[i]), int(s[i-1]+s[i])
            if x1 != 0:
                dp[i+1] += dp[i]
            if 10 <= x2 <= 26:
                dp[i+1] += dp[i-1]
            if not dp[i+1]:
                return 0
        return dp[-1]
        