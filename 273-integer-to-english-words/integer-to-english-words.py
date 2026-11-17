class Solution:
    def numberToWords(self, num: int) -> str:
        if num==0: return "Zero"
        ones=["","One","Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Eleven","Twelve","Thirteen","Fourteen","Fifteen","Sixteen","Seventeen","Eighteen","Nineteen"]
        tens=["","","Twenty","Thirty","Forty","Fifty","Sixty","Seventy","Eighty","Ninety"]
        def three(n):
            r=""
            if n>=100:
                r+=ones[n//100]+" Hundred"
                n%=100
                if n: r+=" "
            if n>=20:
                r+=tens[n//10]
                n%=10
                if n: r+=" "+ones[n]
            elif n>0:
                r+=ones[n]
            return r
        parts=[]
        for div,name in [(10**9,"Billion"),(10**6,"Million"),(10**3,"Thousand")]:
            if num>=div:
                parts.append(three(num//div)+" "+name)
                num%=div
        if num: parts.append(three(num))
        return " ".join(parts)
