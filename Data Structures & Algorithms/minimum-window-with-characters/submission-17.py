class Solution:
    def minWindow(self, s: str, t: str) -> str:
        charsT = defaultdict(int)
        for c in t:
            charsT[c] += 1
        charsS = defaultdict(int)
        need = len(charsT)
        curr = 0
        l = 0
        while l < len(s) and charsT[s[l]] == 0:
            l += 1
        if l == len(s):
            return ""
        charsS[s[l]] += 1
        if charsT[s[l]] and charsT[s[l]] == charsS[s[l]]:
            curr += 1
        r = l
        ans = [-1, -1]
        ansLength = float("inf")
        # while r < len(s):
        #     charsS[s[r]] += 1
        #     if self.containsSubstr(charsS, charsT):
        #         ans = [l, r]
        #         break
        #     r += 1
        # if r == len(s):
        #     return ""
        
        while l < len(s) and r < len(s):
            if curr == need:
                length = r - l + 1
                if length < ansLength:
                    ans = [l, r]
                    ansLength = length
                charsS[s[l]] -= 1
                if charsS[s[l]] < charsT[s[l]]:
                    curr -= 1
                l += 1
                # if l < len(s):
                #     charsS[ord(s[l].lower())-ord("a")] += 1
            elif charsT[s[l]] == 0:
                charsS[s[l]] -= 1
                l += 1
                # if l < len(s):
                #     charsS[ord(s[l].lower())-ord("a")] += 1
            else:
                r += 1
                if r < len(s):
                    charsS[s[r]] += 1
                    if charsT[s[r]] and charsT[s[r]] == charsS[s[r]]:
                        curr += 1
        return s[ans[0]:(ans[1]+1)] if ansLength != float("inf") else ""
    def containsSubstr(self, s, substr):
        for k, v in substr.items():
            if s[k] < v:
                return False
        return True