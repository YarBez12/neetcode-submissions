class Solution:
    # 1st approach
    # def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
    #     graph = defaultdict(list)
    #     words = [beginWord] + wordList
    #     wordsSet = set(wordList)
    #     if endWord not in wordsSet:
    #         return 0
    #     for word in words:
    #         for i in range(len(word)):
    #             for delta in range(26):
    #                 char = chr(ord("a")+delta)
    #                 newWord = word[:i] + char + word[i+1:]
    #                 if newWord in wordsSet:
    #                     graph[word].append(newWord)
        
    #     visited = set()
    #     q = deque()
    #     level = 0
    #     q.append(beginWord)
    #     visited.add(beginWord)
    #     while q:
    #         level += 1
    #         n = len(q)
    #         for i in range(n):
    #             curr = q.popleft()
    #             for neigh in graph[curr]:
    #                 if neigh == endWord:
    #                     return level + 1
    #                 if neigh in visited:
    #                     continue
    #                 visited.add(neigh)
    #                 q.append(neigh)
    #     return 0

    # 2nd approach

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        graph = defaultdict(list)
        words = [beginWord] + wordList
        wordsSet = set(wordList)
        if endWord not in wordsSet:
            return 0
        for word in words:
            for i in range(len(word)):
                newWord = word[:i] + "*" + word[i+1:]
                graph[newWord].append(word)
        
        visited = set()
        q = deque()
        level = 0
        q.append(beginWord)
        visited.add(beginWord)
        while q:
            level += 1
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                for i in range(len(curr)):
                    key = curr[:i] + "*" + curr[i+1:]
                    for neigh in graph[key]:
                        if neigh == endWord:
                            return level + 1
                        if neigh in visited:
                            continue
                        visited.add(neigh)
                        q.append(neigh)
        return 0


        