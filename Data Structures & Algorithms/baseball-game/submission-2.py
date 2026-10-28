class Solution:
    def calPoints(self, operations: List[str]) -> int:
        st = []
        ans = 0
        for operation in operations:
            if operation.lstrip('-').isdigit():
                st.append(int(operation))
                ans += int(operation)
            elif operation == "+":
                new = st[-1] + st[-2]
                st.append(new)
                ans += new
            elif operation == "D":
                new = st[-1] * 2
                st.append(new)
                ans += new
            else:
                ans -= st[-1]
                st.pop()
        return ans
        