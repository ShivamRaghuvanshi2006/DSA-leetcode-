class Solution:
    def replaceNonCoprimes(self, nums):
        import math
        st=[]
        for x in nums:
            cur=x
            while st:
                g=math.gcd(st[-1],cur)
                if g==1:
                    break
                cur=st.pop()*cur//g
            st.append(cur)
        return st
