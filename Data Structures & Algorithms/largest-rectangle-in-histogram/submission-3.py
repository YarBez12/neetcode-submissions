class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        lefts = [0] * n
        rights = [n-1] * n
        st = []
        for i in range(n):
            while st and heights[i] < heights[st[-1]]:
                last = st.pop()
                rights[last] = i-1
            st.append(i)
        st = []
        for i in range(n):
            while st and heights[i] <= heights[st[-1]]:
                last = st.pop()
                # lefts[last] = i+1
            if not st:
                lefts[i] = 0
            else:
                lefts[i] = st[-1]+1
            st.append(i)

        ans = 0
        for i in range(n):
            width = rights[i] - lefts[i] + 1
            ans = max(ans, width * heights[i])
        return ans
        