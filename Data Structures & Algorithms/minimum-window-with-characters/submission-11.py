class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charsT = defaultdict(int)
        for c in t:
            charsT[c] += 1
        charsS = defaultdict(int)
        l = 0
        while l < len(s) and charsT[s[l]] == 0:
            l += 1
        if l == len(s):
            return ""
        r = l
        ans = []
        while r < len(s):
            charsS[s[r]] += 1
            if self.containsSubstr(charsS, charsT):
                ans = [l, r]
                break
            r += 1
        if r == len(s):
            return ""
        
        while l < len(s) and r < len(s):
            if self.containsSubstr(charsS, charsT):
                m = ans[1] - ans[0] + 1
                curr = r - l + 1
                if curr < m:
                    ans = [l, r]
                charsS[s[l]] -= 1
                l += 1
                # if l < len(s):
                #     charsS[ord(s[l].lower())-ord("a")] += 1
            elif charsT[s[l]] == 0:
                l += 1
                # if l < len(s):
                #     charsS[ord(s[l].lower())-ord("a")] += 1
            else:
                r += 1
                if r < len(s):
                    charsS[s[r]] += 1
        return s[ans[0]:(ans[1]+1)]
    def containsSubstr(self, s, substr):
        for k, v in substr.items():
            if s[k] < v:
                return False
        return True