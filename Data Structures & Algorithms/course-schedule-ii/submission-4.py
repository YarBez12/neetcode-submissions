class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visited = [0] * numCourses
        graph = defaultdict(list)
        ans = []
        for parent, child in prerequisites: 
            graph[parent].append(child)
        for course in range(numCourses):
            if visited[course] == 0:
                if not self.dfs(visited, graph, numCourses, course, ans):
                    return []
        return ans
    
    def dfs(self, visited, graph, numCourses, course, ans):
        visited[course] = 1
        for neigh in graph[course]:
            if visited[neigh] == 1:
                return False
            elif visited[neigh] == 0 and not self.dfs(visited, graph, numCourses, neigh, ans):
                return False
        visited[course] = 2
        ans.append(course)
        return True
    
        
        