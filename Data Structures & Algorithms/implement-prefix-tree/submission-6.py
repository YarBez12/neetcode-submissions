class PrefixTree:

    def __init__(self, isEnd=False, children=None):
        self.isEnd = isEnd
        self.children = children if children is not None else [None] * 26

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            c = curr.children[ord(word[i])-ord("a")]
            if c:
                c.isEnd = c.isEnd or (i == len(word) - 1)
                curr = c
            else:
                newNode = PrefixTree(i == len(word) - 1)
                curr.children[ord(word[i])-ord("a")] = newNode
                curr = newNode


    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            c = curr.children[ord(w)-ord("a")]
            if c:
                curr = c
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for w in prefix:
            c = curr.children[ord(w)-ord("a")]
            if c:
                curr = c
            else:
                return False
        return True
        