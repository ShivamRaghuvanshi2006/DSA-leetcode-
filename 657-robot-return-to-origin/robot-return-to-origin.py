class Solution:
    def judgeCircle(self, m):
        return m.count('U') == m.count('D') and m.count('L') == m.count('R')
