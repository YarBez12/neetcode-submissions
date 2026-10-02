class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        s = "00" + s
        dp = [0] * len(s)
        dp[0] = 1
        dp[1] = 1
        for i in range(2, len(s)):
            x1, x2 = int(s[i]), int(s[i-1]+s[i])
            if x1 != 0:
                dp[i] += dp[i-1]
            if 10 <= x2 <= 26:
                dp[i] += dp[i-2]
            if not dp[i]:
                return 0
        return dp[-1]
        