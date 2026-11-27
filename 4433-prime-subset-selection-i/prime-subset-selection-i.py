class Solution:
    def maxPrimes(self, n: int, s: int) -> list[int]:
        if n < 2:
            return []
        is_p = bytearray(b'\x01') * (n + 1)
        is_p[0:2] = b'\x00\x00'
        import math
        for p in range(2, int(math.isqrt(n)) + 1):
            if is_p[p]:
                step = p
                start = p * p
                is_p[start:n+1:step] = b'\x00' * ((n - start) // step + 1)
        res = []
        total = 0
        for p in range(2, n + 1):
            if is_p[p]:
                if total + p > s:
                    break
                total += p
                res.append(p)
        return res