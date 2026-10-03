class Solution:
    # dfs approach

    # def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    #     visited = [0] * numCourses
    #     graph = defaultdict(list)
    #     ans = []
    #     for parent, child in prerequisites: 
    #         graph[parent].append(child)
    #     for course in range(numCourses):
    #         if visited[course] == 0:
    #             if not self.dfs(visited, graph, numCourses, course, ans):
    #                 return []
    #     return ans
    
    # def dfs(self, visited, graph, numCourses, course, ans):
    #     visited[course] = 1
    #     for neigh in graph[course]:
    #         if visited[neigh] == 1:
    #             return False
    #         elif visited[neigh] == 0 and not self.dfs(visited, graph, numCourses, neigh, ans):
    #             return False
    #     visited[course] = 2
    #     ans.append(course)
    #     return True

    # bfs approach

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        ans = []
        indegree = [0] * numCourses
        graph = defaultdict(list)
        for child, parent in prerequisites: 
            graph[parent].append(child)
            indegree[child] += 1
        q = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
        taken = 0
        while q:
            curr = q.popleft()
            ans.append(curr)
            taken += 1
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if not indegree[neigh]:
                    q.append(neigh)
        return ans if taken == numCourses else []
    
    
        
        