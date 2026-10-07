class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = []
        for i in range(len(edges)):
            parents.append(i+1)
        for edge in edges:
            v1, v2 = edge
            p1 = self.findParent(parents, v1)
            p2 = self.findParent(parents, v2)
            if p1 == p2:
                return edge
            parents[p2-1] = p1
        return []
    
    def findParent(self, parents, node):
        curr = node
        while curr != parents[curr-1]:
            curr = parents[curr-1]
        return curr




    #     visited = set()
    #     graph = defaultdict(list)
    #     for v1, v2 in edges:
    #         graph[v1].append(v2)
    #         graph[v2].append(v1)
    #     return self.dfs(graph, 1, -1, visited)
        


    # def dfs(self, graph, node, parent, visited):
    #     visited.add(node)
    #     for neigh in graph[node]:
    #         if neigh not in visited:
    #             res = self.dfs(graph, neigh, node, visited)
    #             if res:
    #                 return res
    #         elif neigh != parent:
    #             return [min(neigh, node), max(neigh, node)]
    #     return []