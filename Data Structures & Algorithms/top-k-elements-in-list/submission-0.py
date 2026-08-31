class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = defaultdict(int)
        for n in nums:
            m[n] += 1
        h = []
        heapq.heapify(h)
        for key,value in m.items():
            heapq.heappush(h, (value, key))
            if len(h) > k:
                heapq.heappop(h)
        return [value for _, value in h]
        