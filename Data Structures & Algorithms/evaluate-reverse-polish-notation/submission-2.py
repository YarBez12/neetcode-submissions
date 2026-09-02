class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        for token in tokens:
            if token in "+-*/":
                val1 = int(st.pop())
                val2 = int(st.pop())
                if token == "+":
                    st.append(val2 + val1)
                elif token == "-":
                    st.append(val2 - val1)
                elif token == "*":
                    st.append(val2 * val1)
                else:
                    st.append(int(val2 / val1))
            else:
                st.append(token)
        
        return int(st[-1])
        