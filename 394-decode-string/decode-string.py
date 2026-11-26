class Solution:
    def decodeString(self, s: str) -> str:
        st=[]
        cur=""
        k=0
        for ch in s:
            if ch.isdigit():
                k=k*10+int(ch)
            elif ch=='[':
                st.append((cur,k)); cur=""; k=0
            elif ch==']':
                prev,kk=st.pop()
                cur=prev+cur*kk
            else:
                cur+=ch
        return cur