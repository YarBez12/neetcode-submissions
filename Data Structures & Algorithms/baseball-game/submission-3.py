class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ans = 0
        for operation in operations:
            if operation == "+":
                new = st[-1] + st[-2]
                st.append(new)
                ans += new
            elif operation == "D":
                new = st[-1] * 2
                st.append(new)
                ans += new
            elif operation == "C":
                ans -= st[-1]
                st.pop()
            else:
                st.append(int(operation))
                ans += int(operation)
        return ans
        