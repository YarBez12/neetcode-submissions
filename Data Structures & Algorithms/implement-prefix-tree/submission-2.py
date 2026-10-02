class PrefixTree:

    def __init__(self, val="", isEnd=False, children=None):
        self.val = val
        self.isEnd = isEnd
        self.children = children if children is not None else []

    def insert(self, word: str) -> None:
        curr = self
        for i in range(len(word)):
            for c in curr.children:
                if c.val == word[i]:
                    c.isEnd = c.isEnd or (i == len(word) - 1)
                    curr = c
                    break
            else:
                newNode = PrefixTree(word[i], i == len(word) - 1)
                curr.children.append(newNode)
                curr = newNode


    def search(self, word: str) -> bool:
        curr = self
        for w in word:
            for c in curr.children:
                if c.val == w:
                    curr = c
                    break
            else:
                return False
        return curr.isEnd

    def startsWith(self, prefix: str) -> bool:
        curr = self
        for w in prefix:
            for c in curr.children:
                if c.val == w:
                    curr = c
                    break
            else:
                return False
        return True
        