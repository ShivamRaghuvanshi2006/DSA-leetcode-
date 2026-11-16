class Solution:
    def readBinaryWatch(self, n):
        return ['%d:%02d' % (h, m) for h in range(12) for m in range(60) if bin(h).count('1') + bin(m).count('1') == n]
