class Solution:
    def calculate(self, s: str) -> int:
        st=[]; num=0; sign=1; res=0
        for c in s:
            if c.isdigit(): num=num*10+int(c)
            elif c in '+-':
                res+=sign*num; num=0; sign=1 if c=='+' else -1
            elif c=='(':
                st.append(res); st.append(sign); res=0; sign=1
            elif c==')':
                res+=sign*num; num=0
                res*=st.pop(); res+=st.pop()
        return res+sign*num
