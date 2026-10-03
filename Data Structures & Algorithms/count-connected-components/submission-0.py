class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        visited = set()
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        count = 0
        for node in range(n):
            if node not in visited:
                count += 1
                self.dfs(graph, node, visited)
        return count
        

    def dfs(self, graph, node, visited):
        visited.add(node)
        for neigh in graph[node]:
            if neigh not in visited:
                self.dfs(graph, neigh, visited)