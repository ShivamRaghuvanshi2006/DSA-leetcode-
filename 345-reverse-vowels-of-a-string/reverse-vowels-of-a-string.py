class Solution:
    def reverseVowels(self, s):
        v = set('aeiouAEIOU')
        a = list(s)
        l, r = 0, len(a) - 1
        while l < r:
            while l < r and a[l] not in v:
                l += 1
            while l < r and a[r] not in v:
                r -= 1
            a[l], a[r] = a[r], a[l]
            l += 1; r -= 1
        return ''.join(a)
