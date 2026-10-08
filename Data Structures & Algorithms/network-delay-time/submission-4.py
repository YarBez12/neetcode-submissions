class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for u, v, t in times:
            graph[u].append((v, t))

        q = deque()
        dist = {u:float("inf") for u in range(1,n+1)}
        q.append((k,0))
        dist[k] = 0

        while q:
            u, currDist = q.popleft()
            if currDist > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > currDist + w:
                    dist[v] = currDist + w
                    q.append((v, dist[v]))
        
        ans = max(dist.values())
        return ans if ans != float("inf") else -1