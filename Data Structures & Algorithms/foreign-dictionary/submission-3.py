class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        graph, indegree, isValid = self.getGraph(words)
        if not isValid:
            return ""
        q = deque()
        n = len(indegree)
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
            elif indegree[i] == -1:
                n -= 1
        ans = []
        while q:
            curr = q.popleft()
            currLetter = chr(ord("a")+curr)
            ans.append(currLetter)
            for neigh in graph[curr]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
        return "".join(ans) if len(ans) == n else ""

    def getGraph(self, words):
        graph = [None] * 26
        indegree = [-1] * 26
        for word in words:
            for w in word:
                i = ord(w) - ord("a")
                graph[i] = set()
                indegree[i] = 0
        for i in range(len(words)-1):
            ch1, ch2, isValid = self.findLetterOrder(words[i], words[i+1])
            if not isValid:
                return [], [], False
            if ch1 == ch2 == "":
                continue
            ch1 = ord(ch1) - ord("a")
            ch2 = ord(ch2) - ord("a")
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


            
            

        