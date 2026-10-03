class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = defaultdict(list)
        visited = set()
        for v1, v2 in edges:
            graph[v1].append(v2)
            graph[v2].append(v1)
        self.dfs(graph, 0, visited)
        return len(visited) == n and len(edges) == n -1
        

    def dfs(self, graph, node, visited):
        if node in visited:
            return 
        visited.add(node)
        for neigh in graph[node]:
            self.dfs(graph, neigh, visited)
        