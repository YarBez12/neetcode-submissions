class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        ans = []
        def backtrack(curr, currSum, ind, ans):
            if ind >= len(candidates):
                return
            prev = -1
            for i in range(ind, len(candidates)):
                if prev == candidates[i]:
                    continue
                if currSum + candidates[i] > target:
                    break
                curr.append(candidates[i])
                currSum += candidates[i]
                if currSum == target:
                    ans.append(curr.copy())
                backtrack(curr, currSum, i+1, ans)
                curr.pop()
                currSum -= candidates[i]
                prev = candidates[i]
        
        backtrack([], 0, 0, ans)
        return ans
        