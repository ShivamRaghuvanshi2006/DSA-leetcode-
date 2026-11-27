import math
class Solution:
    def threeFibonacciSum(self, n: int) -> bool:
        import math
        if n % 2 == 1:
            return False
        x = n // 2
        if x <= 0:
            return False
        def is_square(v):
            r = math.isqrt(v)
            return r*r == v
        return is_square(5*x*x+4) or is_square(5*x*x-4)