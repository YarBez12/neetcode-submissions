class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #1st approach 

        # n = len(heights)
        # lefts = [0] * n
        # rights = [n-1] * n
        # st = []
        # for i in range(n):
        #     while st and heights[i] < heights[st[-1]]:
        #         last = st.pop()
        #         rights[last] = i-1
        #     st.append(i)
        # st = []
        # for i in range(n):
        #     while st and heights[i] <= heights[st[-1]]:
        #         last = st.pop()
        #         # lefts[last] = i+1
        #     if not st:
        #         lefts[i] = 0
        #     else:
        #         lefts[i] = st[-1]+1
        #     st.append(i)

        # ans = 0
        # for i in range(n):
        #     width = rights[i] - lefts[i] + 1
        #     ans = max(ans, width * heights[i])
        # return ans

        #2nd approach

        maxArea = 0
        stack = []
        n = len(heights)
        for i in range(n+1):
            currHeight = heights[i] if i != n else 0
            while stack and currHeight < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1 if stack else i
                maxArea = max(maxArea, height * width)
            stack.append(i)
        return maxArea
        