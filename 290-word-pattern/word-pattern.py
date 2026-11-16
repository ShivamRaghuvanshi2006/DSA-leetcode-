class Solution:
    def wordPattern(self, pattern, s):
        w = s.split()
        return len(set(zip(pattern, w))) == len(set(pattern)) == len(set(w)) and len(pattern) == len(w)
