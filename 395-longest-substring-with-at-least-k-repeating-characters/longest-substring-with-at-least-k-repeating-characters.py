class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        from collections import Counter
        def helper(s):
            if len(s)<k: return 0
            c=Counter(s)
            for ch,f in c.items():
                if f<k:
                    return max(helper(p) for p in s.split(ch))
            return len(s)
        return helper(s)