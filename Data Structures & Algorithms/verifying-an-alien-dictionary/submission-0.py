class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderDict = {order[i]: i for i in range(len(order))}
        for i in range(len(words)-1):
            if not self.check(words[i], words[i+1], orderDict):
                return False
        return True

    def check(self, word1, word2, order):
        for i in range(len(word1)):
            if i >= len(word2) or order[word1[i]] > order[word2[i]]:
                return False
            if order[word1[i]] < order[word2[i]]:
                return True
        return True