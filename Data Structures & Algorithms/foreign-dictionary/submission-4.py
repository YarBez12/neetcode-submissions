class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph, indegree, isValid = self.getGraph(words)
        if not isValid:
            return ""
        q = deque()
        n = len(indegree)
        for i in indegree:
            if indegree[i] == 0:
                q.append(i)
        ans = []
        while q:
            curr = q.popleft()
            ans.append(curr)
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return "".join(ans) if len(ans) == n else ""

    def getGraph(self, words):
        graph = {}
        indegree = {}
        for word in words:
            for w in word:
                graph[w] = set()
                indegree[w] = 0
        for i in range(len(words)-1):
            ch1, ch2, isValid = self.findLetterOrder(words[i], words[i+1])
            if not isValid:
                return [], [], False
            if ch1 == ch2 == "":
                continue
            if ch1 in graph[ch2]:
                return [], [], False
            if ch2 not in graph[ch1]:
                graph[ch1].add(ch2)
                indegree[ch2] += 1
        return graph, indegree, True

    def findLetterOrder(self, word1, word2):
        i = 0
        n1 = len(word1)
        n2 = len(word2)
        while i < n1 and i < n2:
            if word1[i] != word2[i]:
                return word1[i], word2[i], True
            i +=1
        if n1 > n2:
            return "", "", False
        return "", "", True


            
            

        