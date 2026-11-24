class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal): return False
        if s==goal: return len(set(s))<len(s)
        d=[(a,b) for a,b in zip(s,goal) if a!=b]
        return len(d)==2 and d[0]==d[1][::-1]