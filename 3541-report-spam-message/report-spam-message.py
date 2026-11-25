class Solution:
    def reportSpam(self, message, bannedWords):
        b=set(bannedWords)
        return sum(1 for w in message if w in b)>=2
