class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        chars = {}
        ans = 0
        for i in range(len(s)):
            c = s[i]
            if c in chars and l <= chars[c]:
                ans = max(ans, i-l)
                l = chars[c]+1
                chars[c] = i
            else:
                chars[c] = i
        ans = max(ans, len(s)-l)
        return ans
        