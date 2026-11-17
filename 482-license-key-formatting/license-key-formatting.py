class Solution:
    def licenseKeyFormatting(self, s, k):
        t = ''.join(s.split('-')).upper()
        r = []
        while t:
            r.append(t[-k:])
            t = t[:-k]
        return '-'.join(reversed(r))
