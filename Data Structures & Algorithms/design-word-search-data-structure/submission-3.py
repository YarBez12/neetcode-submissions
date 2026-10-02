class TrieNode:
    def __init__(self, isEnd=False, children=None):
        self.isEnd = isEnd
        self.children = children if children is not None else [None] * 26


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for i in range(len(word)):
            ind = ord(word[i])-ord("a")
            c = curr.children[ind]
            if not curr.children[ind]:
                curr.children[ind] = TrieNode()
            curr = curr.children[ind]
        curr.isEnd = True

    def search(self, word: str) -> bool:
        return self.recSearch(self.root, word, 0)
    
    def recSearch(self, node, word, ind):
        if len(word) == ind:
            return node.isEnd
        if word[ind] == ".":
            for ch in node.children:
                if ch != None and self.recSearch(ch, word, ind+1):
                    return True
            return False
        else:
            i = node.children[ord(word[ind])-ord("a")]
            return i != None and self.recSearch(i, word, ind+1)

        