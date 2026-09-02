class Solution:
    def trap(self, height: List[int]) -> int:
        maxInd = 0
        for i in range(len(height)):
            if height[i] > height[maxInd]:
                maxInd = i
        l = 0
        r = len(height) - 1
        ans = 0
        # curr = height[l]
        i = 0
        while l < maxInd:
            if height[i] < height[l]:
                ans += height[l] - height[i]
            else:
                l = i
            i += 1
        
        i = r
        while r > maxInd:
            if height[i] < height[r]:
                ans += height[r] - height[i]
            else:
                r = i
            i -= 1
        return ans