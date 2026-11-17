class Solution:
    def countDigitOne(self, n: int) -> int:
        c=0; f=1
        while f<=n:
            h=n//(f*10); cur=(n//f)%10; lo=n%f
            if cur==0: c+=h*f
            elif cur==1: c+=h*f+lo+1
            else: c+=(h+1)*f
            f*=10
        return c
