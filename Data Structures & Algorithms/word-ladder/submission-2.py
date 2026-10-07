class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        words = [beginWord] + wordList
        wordsSet = set(wordList)
        for word in words:
            for i in range(len(word)):
                for delta in range(26):
                    char = chr(ord("a")+delta)
                    newWord = word[:i] + char + word[i+1:]
                    if newWord in wordsSet:
                        graph[newWord].append(word)
                        graph[word].append(newWord)
        
        visited = set()
        q = deque()
        level = 0
        q.append(beginWord)
        while q:
            level += 1
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                for neigh in graph[curr]:
                    if neigh == endWord:
                        return level + 1
                    if neigh in visited:
                        continue
                    visited.add(neigh)
                    q.append(neigh)
        return 0


        