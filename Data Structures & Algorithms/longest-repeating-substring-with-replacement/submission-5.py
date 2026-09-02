class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        ans = 0
        counts = defaultdict(int)
        maxOcc = 0
        for i in range(len(s)):
            c = s[i]
            counts[c] += 1
            if counts[c] > maxOcc:
                maxOcc = counts[c]
            while l < len(s) and (i-l+1) - maxOcc > k:
                counts[s[l]] -= 1
                l += 1
            ans = max(ans, i-l+1)
        
        return ans

        