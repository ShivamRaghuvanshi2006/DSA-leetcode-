class Solution:
    def longestPalindrome(self, s):
        from collections import Counter
        c = Counter(s)
        l = sum(v // 2 * 2 for v in c.values())
        return l + (1 if l < len(s) else 0)
