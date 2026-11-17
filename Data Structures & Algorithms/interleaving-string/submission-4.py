class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n = len(s1)
        m = len(s2)
        if len(s3) != n + m:
            return False
        dp = [[False] * (m+1) for i in range(n+1)]
        dp[0][0] = True

        for i in range(n+1):
            for j in range(m+1):
                lastInd = i+j-1
                if i > 0 and s3[lastInd] == s1[i-1]:
                    dp[i][j] = dp[i][j] or dp[i-1][j]
                if j > 0 and s3[lastInd] == s2[j-1]:
                    dp[i][j] = dp[i][j] or dp[i][j-1]
        return dp[-1][-1]

        