class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.backtrack(n, 0, 0, "", ans)
        return ans


    def backtrack(self, n, nOpen, nClosed, curr, ans):
        if len(curr) == n * 2:
            ans.append(curr)
            return
        if nOpen != n:
            self.backtrack(n, nOpen+1, nClosed, curr + "(", ans)
        if nOpen != nClosed:
            self.backtrack(n, nOpen, nClosed+1, curr + ")", ans)
        