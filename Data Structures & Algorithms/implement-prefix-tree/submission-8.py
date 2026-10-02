class TrieNode:
    def __init__(self, isEnd=False, children=None):
        self.isEnd = isEnd
        self.children = children if children is not None else [None] * 26

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            ind = ord(word[i])-ord("a")
            c = curr.children[ind]
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.isEnd = True


    def find(self, word):
        curr = self.root
        for w in word:
            c = curr.children[ord(w)-ord("a")]
            if c:
                curr = c
            else:
                return None
        return curr
    def search(self, word: str) -> bool:
        node = self.find(word)
        return node != None and node.isEnd

    def startsWith(self, prefix: str) -> bool:
        node = self.find(prefix)
        return node != None
        