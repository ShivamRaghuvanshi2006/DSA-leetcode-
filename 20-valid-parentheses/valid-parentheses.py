class Solution:
    def isValid(self, s):
        m={')':'(',']':'[','}':'{'}
        st=[]
        for ch in s:
            if ch in '([{':
                st.append(ch)
            else:
                if not st or st.pop()!=m[ch]:
                    return False
        return not st
