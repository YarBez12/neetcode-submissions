class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for s, d, cost in flights:
            graph[s].append((d, cost))
        
        stops = {v: float("inf") for v in range(n)}
        h = [(0, 0, src)]
        while h:
            currDist, usedStops, v = heapq.heappop(h)
            if v == dst:
                return currDist
            if usedStops > k or stops[v] <= usedStops:
                continue
            stops[v] = usedStops
            for u, w in graph[v]:
                heapq.heappush(h, (currDist + w, usedStops+1, u))
        
        return -1
        