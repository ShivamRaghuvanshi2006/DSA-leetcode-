class Solution:
    def singleNumber(self, nums):
        ones=twos=0
        for x in nums:
            ones=(ones^x)&~twos
            twos=(twos^x)&~ones
        return ones