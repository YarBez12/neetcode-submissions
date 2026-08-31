class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        m = defaultdict(int)
        for c in s:
            m[c] += 1
        for c in t:
            if not m[c]:
                return False
            m[c] -= 1
            if m[c] == 0:
                del m[c]
        return len(m) == 0
            
        