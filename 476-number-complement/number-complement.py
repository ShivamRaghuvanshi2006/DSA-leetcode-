class Solution:
    def findComplement(self, num):
        m = 1
        while m <= num:
            m <<= 1
        return (m - 1) ^ num
