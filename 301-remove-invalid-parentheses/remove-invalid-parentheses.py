from collections import deque
class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def valid(t):
            b=0
            for c in t:
                if c=='(': b+=1
                elif c==')':
                    b-=1
                    if b<0: return False
            return b==0
        q=deque([s]); seen={s}; ans=[]
        while q:
            for _ in range(len(q)):
                u=q.popleft()
                if valid(u):
                    ans.append(u)
                if ans: continue
                for i,ch in enumerate(u):
                    if ch not in '()': continue
                    v=u[:i]+u[i+1:]
                    if v not in seen:
                        seen.add(v); q.append(v)
            if ans: return ans
        return [""]
