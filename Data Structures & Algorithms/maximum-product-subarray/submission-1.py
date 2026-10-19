class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        currMax = 1
        currMin = 1

        ans = max(nums)

        for num in nums:
            if num == 0:
                currMax = 1
                currMin = 1
                continue
            t = currMax
            currMax = max(currMax * num, num, currMin * num)
            currMin = min(t * num, num, currMin * num)
            ans = max(ans, currMax)
        return ans