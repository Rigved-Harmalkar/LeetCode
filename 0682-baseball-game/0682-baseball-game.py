class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = ['C','D','+']
        st = []

        for op in operations:
            if op not in ops:
                st.append(int(op))
            else:
                if op == 'C':
                    st.pop()
                elif op == 'D':
                    st.append(int(st[-1])*2)
                else:
                    if len(st) >= 2:
                        st.append(st[-1] + st[-2])
        return sum(st)

