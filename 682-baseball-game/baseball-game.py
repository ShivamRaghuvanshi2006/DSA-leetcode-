class Solution:
    def calPoints(self, ops):
        st = []
        for o in ops:
            if o == 'C': st.pop()
            elif o == 'D': st.append(2 * st[-1])
            elif o == '+': st.append(st[-1] + st[-2])
            else: st.append(int(o))
        return sum(st)
