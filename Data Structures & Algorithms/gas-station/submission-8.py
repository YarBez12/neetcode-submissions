class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # total = 0
        # for i in range(len(gas)):
        #     total += gas[i] -cost[i]
        #     if total >= 0:
        #         return i
        # return -1
        total = 0
        curr = 0
        max = -1
        for i in range(len(gas)):
            delta = gas[i] -cost[i]
            curr += delta
            if delta >= 0 and (curr-delta < 0 or max == -1):
                max =i
                curr = 0
            total += delta
        return max if total >= 0 else -1
        