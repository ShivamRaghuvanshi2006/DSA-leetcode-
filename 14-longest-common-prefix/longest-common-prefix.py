class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return ""
        p=strs[0]
        for s in strs[1:]:
            while not s.startswith(p):
                p=p[:-1]
                if not p:
                    return ""
        return p
