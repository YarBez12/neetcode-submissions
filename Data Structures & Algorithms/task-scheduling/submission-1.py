class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        maxCount = 0
        maxNum = 0
        counts = [0] * 26
        for task in tasks:
            i = ord(task) - ord("A")
            counts[i] += 1
            if counts[i] > maxCount:
                maxCount = counts[i]
                maxNum = 1
            elif counts[i] == maxCount:
                maxNum += 1
        ans = (n+1) * (maxCount-1) + maxNum
        return ans if ans > len(tasks) else len(tasks)
        