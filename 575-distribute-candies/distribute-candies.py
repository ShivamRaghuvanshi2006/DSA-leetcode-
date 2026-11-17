class Solution:
    def distributeCandies(self, c):
        return min(len(set(c)), len(c) // 2)
