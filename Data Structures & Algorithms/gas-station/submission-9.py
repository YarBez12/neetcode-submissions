class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total = 0
        curr = 0
        max = 0
        for i in range(len(gas)):
            delta = gas[i] -cost[i]
            curr += delta
            if curr < 0:
                curr = 0
                max = i +1
            total += delta
        return max if total >= 0 else -1
        