class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        seen = set(deadends)

        q = deque([("0000",0)])
        if "0000" in seen:
            return -1
        seen.add("0000")

        while q:
            curr, count = q.popleft()
            if curr == target:
                return count
            for i in range(len(curr)):
                for delta in (-1,1):
                    nextDigit = (int(curr[i]) + delta) % 10
                    nextStr = curr[:i] + str(nextDigit) + curr[(i+1):]
                    if nextStr not in seen:
                        seen.add(nextStr)
                        q.append((nextStr, count+1))
        return -1
                

            

        