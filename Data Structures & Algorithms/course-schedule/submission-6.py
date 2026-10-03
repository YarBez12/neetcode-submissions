class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = [0] * numCourses
        for i in range(numCourses):
            visited[i] = 0
        graph = defaultdict(list)
        for child, parent in prerequisites: 
            graph[parent].append(child)
        for course in range(numCourses):
            if visited[course] == 0:
                if not self.dfs(visited, graph, numCourses, course):
                    return False
        return True
    
    def dfs(self, visited, graph, numCourses, course):
        visited[course] = 1
        for neigh in graph[course]:
            if visited[neigh] == 1:
                return False
            elif visited[neigh] == 0 and not self.dfs(visited, graph, numCourses, neigh):
                return False
        visited[course] = 2
        return True
    
        
        