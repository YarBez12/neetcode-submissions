class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set()
        deadSet = set(deadends)

        q = deque([("0000",0)])
        seen.add("0000")

        while q:
            curr, count = q.popleft()
            if curr in deadSet:
                continue
            if curr == target:
                return count
            for i in range(len(curr)):
                nextDigit = (int(curr[i]) + 1) % 10
                prevDigit = (int(curr[i]) - 1) % 10
                nextStr = curr[:i] + str(nextDigit) + curr[(i+1):]
                prevStr = curr[:i] + str(prevDigit) + curr[(i+1):]
                if nextStr not in seen:
                    seen.add(nextStr)
                    q.append((nextStr, count+1))
                if prevStr not in seen:
                    seen.add(prevStr)
                    q.append((prevStr, count+1))
        return -1
                

            

        