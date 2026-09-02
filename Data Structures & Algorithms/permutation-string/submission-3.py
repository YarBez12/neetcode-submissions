class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        f1 = [0] * 26
        f2 = [0] * 26
        for c in s1:
            f1[ord(c)-ord("a")] += 1
        l = 0
        r = len(s1)-1
        for c in s2[:len(s1)]:
            f2[ord(c)-ord("a")] += 1
        # Add check here
        while r < len(s2):
            # found = False
            # for i in range(len(f1)):
            #     if f1[i] != f2[i]:
            #         found = True
            #         break
            # if not found:
            #     return True
            if f1 == f2:
                return True
            f2[ord(s2[l])-ord("a")] -=1
            l += 1
            r += 1
            if r < len(s2):
                f2[ord(s2[r])-ord("a")] +=1
        return False
        