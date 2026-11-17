class Solution:
    def detectCapitalUse(self, w):
        return w.isupper() or w.islower() or w.istitle()
