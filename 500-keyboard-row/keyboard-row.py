class Solution:
    def findWords(self, words):
        rows = [set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')]
        res = []
        for w in words:
            s = set(w.lower())
            if any(s <= r for r in rows):
                res.append(w)
        return res
