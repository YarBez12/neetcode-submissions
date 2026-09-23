class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for p in points:
            x,y = p
            dist = -(x**2 + y**2)
            if len(heap) < k:
                heapq.heappush(heap, (dist,p))
            elif heap[0][0] < dist:
                heapq.heappop(heap)
                heapq.heappush(heap, (dist,p))
        ans = [point for _, point in heap]
        return ans