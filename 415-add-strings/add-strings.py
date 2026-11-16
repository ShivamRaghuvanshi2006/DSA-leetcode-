class Solution:
    def addStrings(self, a, b):
        i, j, c, r = len(a)-1, len(b)-1, 0, ''
        while i >= 0 or j >= 0 or c:
            s = c
            if i >= 0:
                s += ord(a[i]) - 48; i -= 1
            if j >= 0:
                s += ord(b[j]) - 48; j -= 1
            r = chr(s % 10 + 48) + r
            c = s // 10
        return r
