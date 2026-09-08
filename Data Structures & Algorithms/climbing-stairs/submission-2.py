class Solution:
    def climbStairs(self, n: int) -> int:
        # 1st approach

        # arr = [1,1,2]
        # if n <= 2:
        #     return arr[n]
        # for i in range(3,n+1):
        #     arr.append(arr[i-2]+arr[i-1])
        # return arr[-1]

        # 2nd approach
        
        if n <=1:
            return 1
        p1 = 1
        p2 = 1
        for i in range(2,n+1):
            t = p1+p2
            p2 = p1
            p1 = t
        return p1
        