class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s = s + s
        
        alt_01 = "".join("0" if i % 2 == 0 else "1" for i in range(2 * n))
        alt_10 = "".join("1" if i % 2 == 0 else "0" for i in range(2 * n))

        patterns_01 = 0
        patterns_10 = 0
        ans = n

        left = 0

        for right in range(n * 2):
            if s[right] != alt_01[right]:
                patterns_01 += 1
            if s[right] != alt_10[right]:
                patterns_10 += 1

            if right - left >= n:
                if s[left] != alt_01[left]:
                    patterns_01 -= 1
                if s[left] != alt_10[left]:
                    patterns_10 -= 1
                left += 1
                ans = min(ans, patterns_01, patterns_10)
        return ans