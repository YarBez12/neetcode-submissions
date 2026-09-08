class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #1st approach 

        # ans = [0,0]
        # for i in range(2,len(cost)+1):
        #     ans.append(min(ans[i-2]+cost[i-2], ans[i-1]+cost[i-1]))
        # return ans[-1]

        #2nd approach 
        
        if len(cost) == 0:
            return 0
        p1 = 0
        p2 = 0
        for i in range(2,len(cost)+1):
            t = min(p2 + cost[i-2], p1+cost[i-1])
            p2 = p1
            p1 = t
        return p1
        