class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitsMap = {
            "2" : "abc",
            "3" : "def",
            "4" : "ghi",
            "5" : "jkl",
            "6" : "mno",
            "7" : "pqrs",
            "8" : "tuv",
            "9" : "wxyz",
        }
        ans = []
        self.backtrack(digitsMap, digits, 0, "", ans)
        return ans
    


    def backtrack(self, digitsMap, digits, ind, curr, ans):
        if len(curr) == len(digits):
            ans.append(curr)
            return
        currMap = digitsMap[digits[ind]]
        for i in range(len(currMap)):
            curr += currMap[i]
            self.backtrack(digitsMap, digits, ind+1, curr, ans)
            curr = curr[:-1]
        