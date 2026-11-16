class MinStack:
    def __init__(self): self.st=[]
    def push(self, val): self.st.append((val,min(val,self.st[-1][1] if self.st else val)))
    def pop(self): self.st.pop()
    def top(self): return self.st[-1][0]
    def getMin(self): return self.st[-1][1]