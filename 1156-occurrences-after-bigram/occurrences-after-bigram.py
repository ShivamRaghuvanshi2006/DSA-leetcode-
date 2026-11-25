class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> list[str]:
        w=text.split(); r=[]
        for i in range(len(w)-2):
            if w[i]==first and w[i+1]==second: r.append(w[i+2])
        return r