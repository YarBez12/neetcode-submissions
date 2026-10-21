class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndices = {}
        for i in range(len(s)):
            lastIndices[s[i]] = i
        groups = []
        currEnd = 0
        startInd = 0
        for i in range(len(s)):
            currEnd = max(currEnd, lastIndices[s[i]])
            if currEnd == i:
                groups.append(currEnd-startInd+1)
                startInd = i+1
        return groups
        