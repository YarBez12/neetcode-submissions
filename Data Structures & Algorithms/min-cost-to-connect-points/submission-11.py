class Solution:
    # Kruskal's Algorithm
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #     weights = []
    #     for i in range(len(points)):
    #         p1 = tuple(points[i])
    #         for j in range(i+1, len(points)):
    #             p2 = tuple(points[j])
    #             dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    #             weights.append((dist, p1, p2))
    #     weights.sort()
    #     parents = {tuple(point): tuple(point) for point in points}
    #     sumWeight = 0
    #     edges = 0
    #     n = len(points)
    #     for edge in weights:
    #         w, v1, v2 = edge
    #         p1 = self.find(v1, parents)
    #         p2 = self.find(v2, parents)
    #         if p1 != p2:
    #             sumWeight += w
    #             parents[p1] = p2
    #             edges += 1
    #             if edges == len(points) - 1:
    #                 return sumWeight
    #     return sumWeight
        

    # def find(self, v, parents):
    #     while v != parents[v]:
    #         parents[v] = parents[parents[v]]
    #         v = parents[v]
    #     return v


    # # Prim's Algorithm
    # def minCostConnectPoints(self, points: List[List[int]]) -> int:
    #     weights = defaultdict(list)
    #     for i in range(len(points)):
    #         p1 = tuple(points[i])
    #         for j in range(len(points)):
    #             if i == j:
    #                 continue
    #             p2 = points[j]
    #             dist = abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
    #             weights[p1].append((dist, p2))
    #     h = [(0, tuple(points[0]))]
    #     visited = set()
    #     sumWeight = 0
    #     while h:
    #         weight, point = heapq.heappop(h)
    #         if point in visited:
    #             continue
    #         visited.add(point)
    #         sumWeight += weight
    #         for w, v in weights[point]:
    #             if tuple(v) not in visited:
    #                 heapq.heappush(h, (w, tuple(v)))
    #     return sumWeight

    # Prim's Algorithm (optimized)
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = [(0, 0)]
        visited = set()
        sumWeight = 0
        while h:
            weight, pointInd = heapq.heappop(h)
            if pointInd in visited:
                continue
            visited.add(pointInd)
            px, py = points[pointInd]
            sumWeight += weight
            for v in range(len(points)):
                if v not in visited:
                    vx, vy = points[v]
                    dist = abs(px-vx) + abs(py-vy)
                    heapq.heappush(h, (dist, v))
        return sumWeight
        