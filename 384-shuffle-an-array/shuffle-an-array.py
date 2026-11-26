import random
class Solution:
    def __init__(self, nums):
        self.orig=list(nums)
        self.nums=nums
    def reset(self):
        return list(self.orig)
    def shuffle(self):
        a=list(self.orig)
        random.shuffle(a)
        return a