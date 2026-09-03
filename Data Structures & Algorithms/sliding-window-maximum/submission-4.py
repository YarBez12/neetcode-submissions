class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        removed = defaultdict(int)
        h = []

        l = 0
        r = 0
        ans = []
        while r < len(nums):
            heapq.heappush(h, -nums[r])
            if r >= k:
                removed[nums[r-k]] += 1
            if r >= k-1:
                curr = -h[0]
                while curr in removed and removed[curr] > 0:
                    removed[curr] -= 1
                    heapq.heappop(h)
                    curr = -h[0]
                ans.append(curr)
            l += 1
            r += 1
        
        return ans
        