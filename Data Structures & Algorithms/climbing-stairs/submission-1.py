class Solution:
    def climbStairs(self, n: int) -> int:
        arr = [1,1,2]
        if n <= 2:
            return arr[n]
        for i in range(3,n+1):
            arr.append(arr[i-2]+arr[i-1])
        return arr[-1]
        