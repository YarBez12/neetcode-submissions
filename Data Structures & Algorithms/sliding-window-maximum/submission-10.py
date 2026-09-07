class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # 1st approach

        # removed = defaultdict(int)
        # h = []

        # r = 0
        # ans = []
        # while r < len(nums):
        #     heapq.heappush(h, -nums[r])
        #     if r >= k:
        #         removed[nums[r-k]] += 1
        #     if r >= k-1:
        #         curr = -h[0]
        #         while curr in removed and removed[curr] > 0:
        #             removed[curr] -= 1
        #             heapq.heappop(h)
        #             curr = -h[0]
        #         ans.append(curr)
        #     r += 1
        
        # return ans

        # 2nd approach

        q = deque([])

        i = 0
        ans = []
        while i < len(nums):
            while q and nums[i] > nums[q[-1]]:
                q.pop()
            q.append(i)
            if i >= k-1:
                l = i-k+1
                while q[0] < l:
                    q.popleft()
                ans.append(nums[q[0]])
            i += 1
        
        return ans
        