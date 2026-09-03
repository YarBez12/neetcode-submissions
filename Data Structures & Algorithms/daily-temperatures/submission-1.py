class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        st = []
        ans = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while st and temperatures[st[-1]] < temperatures[i]:
                ans[st[-1]] = (i - st[-1])
                st.pop()
            st.append(i)
        return ans
        